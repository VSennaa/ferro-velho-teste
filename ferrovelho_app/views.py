from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.http import JsonResponse
from django.db import transaction
from django.contrib.admin.views.decorators import staff_member_required
from decimal import Decimal
from collections import defaultdict

from .models import Material, Operacao, ItemOperacao
from .forms import MaterialForm, ItemOperacaoForm

# Página de Materiais
@staff_member_required
def material_list_create(request):
    materials = Material.objects.all().order_by('nome')
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('material_list_create')
    else:
        form = MaterialForm()
    return render(request, 'ferrovelho_app/materials.html', {'materials': materials, 'form': form})

@staff_member_required
def material_edit(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('material_list_create')
    else:
        form = MaterialForm(instance=material)
    return render(request, 'ferrovelho_app/material_form.html', {'form': form, 'title': 'Editar Material'})

# Dashboard
@staff_member_required
def dashboard(request):
    capital_total = Operacao.objects.aggregate(total=Sum('valor_total'))['total'] or 0
    operacoes = Operacao.objects.all().order_by('-data_criacao')
    
    # Agrupar materiais por categoria e somar pesos
    resumo = []
    categorias = Material.objects.values_list('categoria', flat=True).distinct()
    
    for cat in categorias:
        materiais = Material.objects.filter(categoria=cat).annotate(total_peso=Sum('itemoperacao__peso_kg'))
        subtotal_categoria = sum(mat.total_peso or 0 for mat in materiais)
        resumo.append({
            'categoria': dict(Material.CATEGORIAS).get(cat, cat),
            'subtotal': subtotal_categoria,
            'materiais': materiais
        })
    
    return render(request, 'ferrovelho_app/dashboard.html', {
        'capital_total': capital_total,
        'resumo': resumo,
        'operacoes': operacoes
    })

# Aba de Operação (PDV)
@staff_member_required
def operacao_pdv(request):
    if 'current_operacao_items' not in request.session:
        request.session['current_operacao_items'] = []
    
    current_items = request.session['current_operacao_items']
    total_acumulado = sum(Decimal(item['subtotal']) for item in current_items)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add_item':
            form = ItemOperacaoForm(request.POST)
            if form.is_valid():
                material = form.cleaned_data['material']
                peso_kg = form.cleaned_data['peso_kg']
                subtotal = material.preco_por_kg * peso_kg
                item_data = {
                    'material_id': material.id,
                    'material_nome': material.nome,
                    'preco_por_kg': str(material.preco_por_kg),
                    'peso_kg': str(peso_kg),
                    'subtotal': str(subtotal),
                }
                current_items.append(item_data)
                request.session['current_operacao_items'] = current_items
                total_acumulado = sum(Decimal(item['subtotal']) for item in current_items)
                return JsonResponse({
                    'status': 'success',
                    'item': item_data,
                    'total_acumulado': str(total_acumulado)
                })
            else:
                return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

        elif action == 'close_compra':
            with transaction.atomic():
                operacao = Operacao.objects.create(valor_total=total_acumulado)
                for item_data in current_items:
                    material = Material.objects.get(id=item_data['material_id'])
                    ItemOperacao.objects.create(
                        operacao=operacao,
                        material=material,
                        peso_kg=Decimal(item_data['peso_kg']),
                        subtotal=Decimal(item_data['subtotal'])
                    )
                request.session['current_operacao_items'] = []
                request.session.modified = True
            return JsonResponse({'status': 'success', 'message': 'Compra fechada com sucesso!'})
    
    form = ItemOperacaoForm()
    return render(request, 'ferrovelho_app/operacao_pdv.html', {
        'form': form,
        'current_items': current_items,
        'total_acumulado': total_acumulado
    })

@staff_member_required
def deletar_operacao(request, pk):
    operacao = get_object_or_404(Operacao, pk=pk)
    operacao.delete()
    return redirect('dashboard')

@staff_member_required
def reset_estoque(request):
    Operacao.objects.all().delete()
    return redirect('dashboard')

from django import forms
from .models import Material, ItemOperacao

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nome', 'tipo', 'preco_por_kg']

class ItemOperacaoForm(forms.ModelForm):
    class Meta:
        model = ItemOperacao
        fields = ['material', 'peso_kg']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['material'].queryset = Material.objects.all().order_by('nome')
from django.db import models
from django.utils import timezone

class Material(models.Model):
    CATEGORIAS = [
        ('Fino', 'Fino'),
        ('Sucata', 'Sucata'),
        ('Outro', 'Outro'),
    ]
    nome = models.CharField(max_length=100, unique=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='Fino')
    preco_por_kg = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} ({self.get_categoria_display()})"

class Operacao(models.Model):
    data_criacao = models.DateTimeField(default=timezone.now)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Operação {self.id} - {self.data_criacao.strftime('%d/%m/%Y %H:%M')}"

class ItemOperacao(models.Model):
    operacao = models.ForeignKey(Operacao, related_name='itens', on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    peso_kg = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.material.nome} - {self.peso_kg} kg"
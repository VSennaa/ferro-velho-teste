from django.db import models
from django.utils import timezone

class Material(models.Model):
    TIPO_CHOICES = [
        ('FINO', 'Fino'),
        ('PESADO', 'Pesado'),
        ('NAO_FERROSO', 'Não-Ferroso'),
    ]
    nome = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='FINO')
    preco_por_kg = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"

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
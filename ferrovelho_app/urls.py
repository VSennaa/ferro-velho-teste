from django.urls import path
from . import views

urlpatterns = [
    # 1. A Raiz do site (O Dashboard principal)
    path('', views.dashboard, name='dashboard'), 
    
    # 2. As rotas que você já tinha
    path('materials/', views.material_list_create, name='material_list_create'),
    path('materials/<int:pk>/edit/', views.material_edit, name='material_edit'),
    path('pdv/', views.operacao_pdv, name='operacao_pdv'),
    path('operacao/<int:pk>/deletar/', views.deletar_operacao, name='deletar_operacao'),
    path('estoque/reset/', views.reset_estoque, name='reset_estoque'),
]

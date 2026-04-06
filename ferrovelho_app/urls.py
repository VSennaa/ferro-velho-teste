from django.urls import path
from . import views

urlpatterns = [
    path('materials/', views.material_list_create, name='material_list_create'),
    path('materials/<int:pk>/edit/', views.material_edit, name='material_edit'),
    path('pdv/', views.operacao_pdv, name='operacao_pdv'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
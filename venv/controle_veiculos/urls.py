from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('veiculos/', views.cadastro_veiculos, name='cadastro_veiculos'),
    path('motoristas/', views.cadastro_motoristas, name='cadastro_motoristas'),
    path('controle/', views.controle_veiculos, name='controle_veiculos'),
]
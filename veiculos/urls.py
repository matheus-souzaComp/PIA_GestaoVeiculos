from django.urls import path
from . import views

urlpatterns = [

    path('', views.veiculos, name="veiculos"),
    path('atualiza_veiculo/', views.att_veiculo, name="atualiza_veiculo"),
    path('update_veiculo/<int:id>', views.update_veiculo, name="update_veiculo"),

]


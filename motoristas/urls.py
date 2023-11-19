from django.urls import path
from . import views

urlpatterns = [

    path('', views.motoristas, name="motoristas"),
    path('atualiza_motorista/', views.att_motorista, name="atualiza_motorista"),
    path('update_motorista/<int:id>', views.update_motorista, name="update_motorista")

]
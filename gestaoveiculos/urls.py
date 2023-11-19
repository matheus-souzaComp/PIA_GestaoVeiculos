
from django.contrib import admin
from django.urls import path,include
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('veiculos/', include('veiculos.urls')),
    path('motoristas/', include('motoristas.urls')),
    path('servicos/', include('servicos.urls')),
    path('', include('login.urls'))
]

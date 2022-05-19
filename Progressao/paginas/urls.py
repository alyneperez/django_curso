from django.urls import path
from .views import PaginaInicial


urlpatterns = [
    #path("endereço/", MinhaView.as_view(), name="nome-da-url"),
    path("inicio/", PaginaInicial.as_view(), name="inicio"),
]
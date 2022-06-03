from django.urls import path
#Importa as views que a gente criou
from .views import PaginaInicial, SobreView

#tem que ser urlpatterns pq é padrão do django
urlpatterns = [
    #path("endereço/", MinhaView.as_view(), name="nome-da-url"),
        #todo path tem endereço, sua_view.as_view() e nome
    path("", PaginaInicial.as_view(), name="index"),
    path("sobre/", SobreView.as_view(), name="sobre"),
]

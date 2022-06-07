from django.urls import path
from .views import CampoCreate, AtividadeCreate
#Importa as views que a gente criou

#tem que ser urlpatterns pq é padrão do django
urlpatterns = [
    path("cadastrar/campo/", CampoCreate.as_view(), name="cadastrar-campo"),
    path("cadastrar/atividade/", AtividadeCreate.as_view(), name="cadastrar-atividade"),
    #path("endereço/", MinhaView.as_view(), name="nome-da-url"),
        #todo path tem endereço, sua_view.as_view() e nome
]

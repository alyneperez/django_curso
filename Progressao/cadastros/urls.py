from django.urls import path
from .views import CampoCreate, AtividadeCreate, StatusCreate, ClasseCreate, CampusCreate
from .views import CampoUpdate, AtividadeUpdate, StatusUpdate, ClasseUpdate, CampusUpdate

# Importa as views que a gente criou

# tem que ser urlpatterns pq é padrão do django
urlpatterns = [
    path("cadastrar/campo/", CampoCreate.as_view(), name="cadastrar-campo"),
    path("cadastrar/atividade/", AtividadeCreate.as_view(), name="cadastrar-atividade"),
    path("cadastrar/status/", StatusCreate.as_view(), name="cadastrar-status"),
    path("cadastrar/classe/", ClasseCreate.as_view(), name="cadastrar-classe"),
    path("cadastrar/campus/", CampusCreate.as_view(), name="cadastrar-campus"),
    
    path("editar/campo/<int:pk>/", CampoUpdate.as_view(), name="editar-campo"),
    path("editar/atividade/<int:pk>/", AtividadeUpdate.as_view(), name="editar-atividade"),
    path("editar/status/<int:pk>/", StatusUpdate.as_view(), name="editar-status"),
    path("editar/classe/<int:pk>/", ClasseUpdate.as_view(), name="editar-classe"),
    path("editar/campus/<int:pk>/", CampusUpdate.as_view(), name="editar-campus"),
    # path("endereço/", MinhaView.as_view(), name="nome-da-url"),
    # todo path tem endereço, sua_view.as_view() e nome
]

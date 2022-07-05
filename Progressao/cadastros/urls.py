from django.urls import path
from .views import CampoCreate, AtividadeCreate, StatusCreate, ClasseCreate, CampusCreate
from .views import CampoUpdate, AtividadeUpdate, StatusUpdate, ClasseUpdate, CampusUpdate
from .views import CampoDelete, AtividadeDelete, StatusDelete, ClasseDelete, CampusDelete
from .views import CampoList, AtividadeList, StatusList, ClasseList, CampusList

# Importa as views que a gente criou
# tem que ser urlpatterns pq é padrão do django
# path("endereço/", MinhaView.as_view(), name="nome-da-url"),
# todo path tem endereço(padrão url), sua_view.as_view() e nome
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
 
   path("excluir/campo/<int:pk>/", CampoDelete.as_view(), name="excluir-campo"),
   path("excluir/atividade/<int:pk>/", AtividadeDelete.as_view(), name="excluir-atividade"),
   path("excluir/status/<int:pk>/", StatusDelete.as_view(), name="excluir-status"),
   path("excluir/classe/<int:pk>/", ClasseDelete.as_view(), name="excluir-classe"),
   path("excluir/campus/<int:pk>/", CampusDelete.as_view(), name="excluir-campus"),

   path("listar/campos/", CampoList.as_view(), name="listar-campos"),
   path("listar/atividades/", AtividadeList.as_view(), name="listar-atividades"),
   path("listar/status/", StatusList.as_view(), name="listar-status"),
   path("listar/classes/", ClasseList.as_view(), name="listar-classes"),
   path("listar/campus/", CampusList.as_view(), name="listar-campus"),
]

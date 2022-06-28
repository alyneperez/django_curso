from django.views.generic.edit import CreateView, UpdateView
from .models import Campo, Atividade, Status, Classe, Campus
from django.urls import reverse_lazy

# Create your views here.
class CampoCreate(CreateView):
    model = Campo
    fields = ["nome", "descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")
    # depois de cadastrado volta pro index


class AtividadeCreate(CreateView):
    model = Atividade
    fields = ["numero", "descricao", "pontos", "detalhes", "campo"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class StatusCreate(CreateView):
    model = Status
    fields = ["nome", "descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class ClasseCreate(CreateView):
    model = Classe
    fields = ["nome", "descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class CampusCreate(CreateView):
    model = Campus
    fields = ["cidade", "endereço", "telefone"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


#################### UPDATE ########################


class CampoUpdate(UpdateView):
    model = Campo
    fields = ["nome", "descrição"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ["numero", "descricao", "pontos", "detalhes", "campo"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class StatusUpdate(UpdateView):
    model = Status
    fields = ["nome", "descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class ClasseUpdate(UpdateView):
    model = Classe
    fields = ["nome", "descricao"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")


class CampusUpdate(UpdateView):
    model = Campus
    fields = ["cidade", "endereço", "telefone"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

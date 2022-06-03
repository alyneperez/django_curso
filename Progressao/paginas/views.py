from django.views.generic import TemplateView

# Create your views here.

# A classe PaginaInicial "extends" TemplateView
class PaginaInicial(TemplateView):
    template_name = "paginas/index.html"
    #Toda classe filha do templateview precisa do
    #atributo abaixo para definir um template a ser renderizado

class SobreView(TemplateView):
    template_name = "paginas/sobre.html"
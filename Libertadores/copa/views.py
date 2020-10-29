from django.shortcuts import render
from . models import Usuario
from django.views import generic

# Create your views here.

def index(request):
    num_Usuarios = Usuario.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_usuarios ': num_Usuarios }
    )
def form(request):
    
    
    return render(
        request,
        'Form.html',
        context={},
    )

def galeria(request):
    
    return render(
        request,
        'Galeria.html',
    )


class UsuarioListView(generic.ListView):
    models = Usuario



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
    
<<<<<<< HEAD

    return render(
        request,
        'form.html',
        
    )
def galeria(request):
    

    return render(
        request,
        'galeria.html',
       
=======
    
    return render(
        request,
        'Form.html',
        context={},
    )

def galeria(request):
    
    return render(
        request,
        'Galeria.html',
>>>>>>> 22797853a16a9c39941318cb8f32cf64cb643fdb
    )


class UsuarioListView(generic.ListView):
    models = Usuario
<<<<<<< HEAD
class UsuarioDetailView(generic.DetailView):
    model = Usuario
=======
>>>>>>> 22797853a16a9c39941318cb8f32cf64cb643fdb



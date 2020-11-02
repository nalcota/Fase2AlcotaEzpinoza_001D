from django.shortcuts import render
from . models import Usuario
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
class UsuarioDetailView(generic.DetailView):
    model = Usuario

class UsuarioCreate(CreateView):
    model= Usuario
    fields= '__all__'

class UsuarioUpdate(UpdateView):
    model= Usuario
    fields= ['rut','first_name','last_name','correo','contraseña','recontraseña','Direccion']

class UsuarioDelete(DeleteView):
    model= Usuario
    success_url = reverse_lazy('index')





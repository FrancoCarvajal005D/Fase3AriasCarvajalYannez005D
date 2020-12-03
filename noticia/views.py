from django.shortcuts import render
from noticia.models import formulario
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
 



def contacto(request):
    
    return render(
        request,
        'contacto.html',
    )

def index(request):
    return render(request, 'index.html')

def quienes_somos(request):
    
    return render(
        request,
        'quienes_somos.html',
    )

def categorias(request):
    
    return render(
        request,
        'categorias.html',
    )


def peticion(request):
    
    return render(
        request,
        'peticion.html',
    )



class ContactoCreate(CreateView):
    model = contacto
    fields = '__all__'
    initial = {'name', 'email', 'telefono', 'message'}

class ContactoUpdate(UpdateView):
    model = contacto
    fields = {'name', 'email', 'telefono', 'message'}

class ContactoDelete(DeleteView):
    model = contacto
    sucess_url = reverse_lazy('contacto')

class ContactoDetailView(generic.DetailView):
    model = contacto

class peticionCreate(CreateView):
    model = peticion
    fields = '__all__'
    initial = {'name', 'email', 'telefono', 'message'}

class peticionUpdate(UpdateView):
    model = peticion
    fields = {'name', 'email', 'telefono', 'message'}

class peticionDelete(DeleteView):
    model = peticion
    sucess_url = reverse_lazy('contacto')

class peticionDetailView(generic.DetailView):
    model = peticion






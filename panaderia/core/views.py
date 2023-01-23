from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def QuienesSomos(request):
    return render(request, 'Quienes somos.html')

def Galería(request):
    return render(request, 'Galería.html')

def contacto(request):
    return render(request, 'contacto.html')

def pasteleria(request):
    return render(request, 'pasteleria.html')

def panaderia(request):
    return render(request, 'panaderia.html')

def bebidas(request):
    return render(request, 'bebidas.html')

def api(request):
    return render(request, 'API.html')

def registro(request):
    return render(request, 'registro.html')

def mostrar(request):
    clientes = Cliente.objects.all()
    datos={
        'clientes':Cliente
    }
    return render(request, 'mostrar.html', datos)
    
def eliminar(request, id):
    cliente = Clientes.objects.get(id=id)
    cliente.delete()
    return redirect('mostrar')


def crear(request):
    if request.method=='POST': 
        clienteform = ClienteForm(request.POST)
        if clienteform.is_valid():
            clienteform.save()     #similar al insert
            return redirect('mostrar')
    else:
        clienteform=ClienteForm()
    return render(request, 'crearCliente.html', {'clienteform': clienteform})
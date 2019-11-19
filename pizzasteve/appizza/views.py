from django.shortcuts import render, redirect
from .models import Ingrediente, Pizza, Tamano
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'appizza/index.html')

def pizzap(request):
    return render(request,'appizza/pizzap.html')

def formulario(request):

    tamano = Tamano.objects.all()
    ing = Ingrediente.objects.all()

    variable = {'tamano':tamano, 'ing':ing}

    if request.POST:
        pi = Pizza()
        pi.nombre = request.POST.get('txtNombrepizza')
        pi.precio = request.POST.get('txtPrecio')
        ingr = Ingrediente()
        ingr.id = request.POST.get('cboi')
        pi.ingredientes = ingr 
        ta = Tamano()
        ta.id = request.POST.get('cbo')
        pi.Tamano = ta

        
        try:
            pi.save()
            variable [ 'mensaje ' ] = 'Guardado'
        except:
            variable [ 'mensaje ' ] = 'no se ha podido guardar :c'


    return render(request,'appizza/formulario.html', variable)

#CRUD 

def listar_pizzas(request):
    pizzas = Pizza.objects.all()
    

    return render(request, 'appizza/listar_pizzas.html', {'pizzas':pizzas} )



def eliminar_pizza(request, id):

    pizza = Pizza.objects.get(id=id)

    try:
        pizza.delete()

        mensaje = "Pizza Eliminada Correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "no se ha podido eliminar"    
        messages.success(request, mensaje)

    return redirect('listar_pizzas')    



def modificar (request,id):
    pi = Pizza.objects.get(id=id)

    ta = Tamano()
    variable = {'pi':pi, 'ta':ta }

    return render(request, 'appizza/modificar.html', variable)

def registro(request):
    return render(request,'appizza/registro.html')
from django.shortcuts import render

from web.formularios.formularioEmpleados import FormularioEmpleados
from web.formularios.formularioPlatos import FormularioPlatos

# Create your views here.

#TODAS LAS VISTAS SON FUNCIONES DE PYTHON

def Home(request):
    return render(request,'home.html')

def Platos(request):
    #Esta vista va a utilizar un formulario de Django
    #DEBO CREAR UN OBJETO DE LA CLASE FormularioPlatos
    formularioPlatos=FormularioPlatos()

    #CREAMOS UN DICCIONARIO PARA ENVIAR EL FORMULARIO AL HTML(TEMPLATE)
    data={
        'formularioPlatos':formularioPlatos
    }
    return render(request,'menuplatos.html',data)


def Empleados(request):

    formularioEmpleados=FormularioEmpleados()
    data={
        'formularioEmpleados':formularioEmpleados
    }
    return render(request,'empleados.html',data)
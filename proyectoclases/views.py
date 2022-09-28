from urllib import request
from django.http import HttpResponse
from datetime import datetime
from django.template import Context,Template

def hola(request):
    return HttpResponse('Hola mundo web')

def calculadora(request):
    num1 = int(input('numero 1: ' ))
    num2 = int(input('numero 2: ' ))
    return HttpResponse(num1 + num2)

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'La fecha y hora actual es {fecha_actual}')

def nacimiento(request,edad):
    fecha = datetime.now().year - edad 
    return HttpResponse(f'Tu fecha de nacimiento para tu {edad} es {fecha}')

def mi_template(request):

    cargar_archivo = open(r'D:\Python\Proyectodjango\templates\template.html', 'r')

    template = Template(cargar_archivo.read())
    cargar_archivo.close()

    contexto = Context()

    template_renderizado= template.render(contexto)

    return HttpResponse(template_renderizado)
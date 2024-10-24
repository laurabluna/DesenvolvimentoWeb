import sys  
from django.conf import settings   
from django.urls import path   
from django.http import HttpResponse   

settings.configure(DEBUG=True, SECRET_KEY='segredo', 
ROOT_URLCONF=__name__)   

def index(request):
    resultado = '<h1>olá, sou a sua tabuada</h1><ul>'
    for i in range(1, 11):
        resultado += f'<li><a href="/tabuada/{i}/">a tabuada do {i}</a></li>'
    resultado += '</ul>'
    return HttpResponse(resultado) 

def tabuada(request, num):
    resultado = '<h1>aqui ta tabuada do {num} </h1>'.format(num)
    for i in range(1, 11):  
        resultado += '<p>{} x {} = {}</p>'.format(num, i, num * i)
    return HttpResponse(resultado)

urlpatterns = [path('', index, name='index'), path('tabuada/<int:num>/', tabuada, name='tabuada'),]


if __name__ == '__main__':   

    from django.core.management import execute_from_command_line   

    execute_from_command_line(sys.argv)   
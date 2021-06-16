from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request,'miApp/index.html',{

    })


#logear user
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


       user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                print('usuario auntenticado')
            else:
                print('usuario no auntenticado')

    return render(request,'users/login.html',{
        
        
    })


def mapa(request):
    return render(request,'miApp/mapa.html',{

    })

def usuarios(request):
    return render(request,'miApp/usuarios.html',{

    })

def login(request):
    return render(request,'miApp/login.html',{

    })
from django.shortcuts import render

def saludo(request):
    return render(request,'saludo.html',{} )

def dinamico(request, name):
    categoria=['diseño', 'Codificacion']
    context={'name': name, 'categories':categoria}
    return render(request,'dinamico.html',context)

def estatico(request):
    return render(request, 'estatico.html', {})

def home(request):
    return render(request,'home.html', {})

def login(request):
    return render(request, 'login.html', {})

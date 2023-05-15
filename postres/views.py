from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,'index.html')

def recetas(request):
    return render(request,'index.html')

def top_10(request):
    return render(request,'index.html')

def saludables(request):
    return render(request,'index.html')

def contacto(request):
    return render(request,"contacto.html")
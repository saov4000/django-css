from django.shortcuts import render

def index(request):
    return render(request,'index.html',{})

def portifolio(request):
    return render(request,'portifolio.html',{})
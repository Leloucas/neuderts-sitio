from django.http import HttpResponse
from django.shortcuts import render
from portfolio.models import Portfolio

def homepage(request):
    portfolios = Portfolio.objects.all().order_by('-date')
    return render(request, 'homepage.html', {'portfolios': portfolios})

def contacto(request):
    if request.method == 'GET':
        return render(request, 'contacto.html')
    elif request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return HttpResponse(nombre)

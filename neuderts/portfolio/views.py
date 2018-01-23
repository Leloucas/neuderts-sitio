from django.shortcuts import render
from .models import Portfolio
from django.http import HttpResponse

# Create your views here.
def portfolio_list(request):
    portfolios = Portfolio.objects.all().order_by('date')
    return render(request, 'portfolio/portfolio_list.html', {'portfolios': portfolios})

def portfolio_detail(request, slug):
    # return HttpResponse(slug)
    portfolio = Portfolio.objects.get(slug=slug)
    return render(request, 'portfolio/portfolio_detail.html', {'portfolio':portfolio})

from django.shortcuts import render,get_object_or_404,redirect

from .models import Portfolio
# Create your views here.


def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio/portfolio.html',{"portfolios":portfolios})

def detail(request, portfolio_id):
    portfolio_detail=get_object_or_404(Portfolio, pk=portfolio_id)
    return render(request,'portfolio/detail.html',{'portfolio':portfolio_detail})
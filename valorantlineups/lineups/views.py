from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'lineups/index.html')

def bind(request):
    return render(request, 'lineups/bind.html')
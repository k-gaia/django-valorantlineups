from django.http import JsonResponse
from django.shortcuts import render

from lineups.models import *
from django.core import serializers 

# Create your views here.

def home(request):
    return render(request, 'lineups/index.html')

def bind(request):
    return render(request, 'lineups/bind.html')

def haven(request):
    return render(request, 'lineups/haven.html')

def lineups_list(request):
    lineup_data = serializers.serialize("json", Lineup.objects.all())
    return JsonResponse({"Lineups": lineup_data})

def child_lineups_list(request):
    child_lineup_data = serializers.serialize("json", ChildLineup.objects.all())
    return JsonResponse({"Child Lineups": child_lineup_data})
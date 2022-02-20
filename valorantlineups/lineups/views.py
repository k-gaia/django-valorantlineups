from django.http import JsonResponse
from django.shortcuts import redirect, render

from lineups.models import *
from django.core import serializers 

from lineups.forms import NewLineupForm

# Create your views here.

def home(request):
    return render(request, 'lineups/index.html')

def bind(request):
    return render(request, 'lineups/bind.html')

def haven(request):
    return render(request, 'lineups/haven.html')

def lineup_creator(request):
    if request.method == 'POST':
        form = NewLineupForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved something")
        else:
            print(form.errors)
            form = NewLineupForm()
            print("blanked")
        return render(request, 'lineups/lineup_creator.html', {form: form})

    else:

        return render(request, 'lineups/lineup_creator.html')

def lineups_list(request):
    lineup_data = serializers.serialize("json", Lineup.objects.all())
    return JsonResponse({"Lineups": lineup_data})

def child_lineups_list(request):
    child_lineup_data = serializers.serialize("json", ChildLineup.objects.all())
    return JsonResponse({"Child Lineups": child_lineup_data})

    
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from lineups.models import *
from django.core import serializers 

from .forms import NewLineupForm, NewChildLineupForm, NewUserForm

from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    return render(request, 'lineups/index.html')

def bind(request):
    return render(request, 'lineups/bind.html')

def haven(request):
    return render(request, 'lineups/haven.html')

def lineup_creator(request):

    # if POST request, save in form object
    if request.method == 'POST':
        form = NewLineupForm(request.POST)

        # check if form is valid, to ensure data integrity
        if form.is_valid():

            #save form to db
            form.save()
        
        # if form is invalid, throw error to console
        else:
            print(form.errors)
            
            # return empty form, breaking POST request
            form = NewLineupForm()
        
        # return
        return render(request, 'lineups/lineup_creator.html', {form: form})

    # if not POST request, redirect to lineup_creator page
    else:

        return render(request, 'lineups/lineup_creator.html')

def pin_creator(request):
    if request.method == 'POST':
        form = NewChildLineupForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved something")
        else:
            print(form.errors)
            form = NewChildLineupForm()
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

def get_latest_childlineup_id(request):
    try:
        latest = ChildLineup.objects.latest('id')
    except:
        print("db is empty")

    return HttpResponse(latest)

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information")
    form = NewUserForm()
    return render (request=request, template_name="lineups/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="lineups/login.html", context={"login_form":form})

    
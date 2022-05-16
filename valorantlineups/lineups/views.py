from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from lineups.models import *
from django.core import serializers 

from .forms import NewLineupForm, NewChildLineupForm, NewUserForm

from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    return render(request, 'lineups/index.html')

def bind(request):

    context = list(Agent.objects.values())

    #test = {"data": context}

    #print(test["data"][0]["name"])

    return render(request, 'lineups/bind.html', {'data': context})

def haven(request):
    return render(request, 'lineups/haven.html')

def split(request):
    return render(request, 'lineups/split.html')

def ascent(request):
    return render(request, 'lineups/ascent.html')

def lineup_creator(request):

    context = list(Map.objects.values())

    #test = {"data": context}

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

        return render(request, 'lineups/lineup_creator.html', {'data': context})

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

    # if request is post, create populate new user details in form
    # populated from the <form> tags within the regsiter view-template
    if request.method == "POST":
        form = NewUserForm(request.POST)

        # check forms validity, save form, feedback success message
        # redirect to homepage
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")

        # if not valid, feedback error message    
        messages.error(request, "Unsuccessful registration. Invalid information")

    # if not post request, blank form, and take to register page    
    form = NewUserForm()
    return render (request=request, template_name="lineups/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
        
        # get the cleaned data after ensuring the data is valid
        # authenticate cleaned data, in the case the user exists login and send message
        # if the user doesn't exist feedback that it is an invalid username/password
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
	form = AuthenticationForm()
	return render(request=request, template_name="lineups/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")  
	return redirect("home")

def agents_list(request):
    #agents = Agent.objects.values_list('name', flat=True)
    #print(list(agents))
    #return JsonResponse({"Agents": list(agents)})

    agents = list(Agent.objects.values())

    return JsonResponse(agents, safe=False)

    
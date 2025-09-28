from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import login, logout
# Create your views here.


def index(request):
    return render(request, 'accounts/base.html')

def regular(request):
    return HttpResponse("Regular page sanity checks")

def landlord(request):
    return HttpResponse("Landlord page sanity checks")

def landlord_signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            landlord_group, _ = Group.objects.get_or_create(name="Landlord")
            user.groups.add(landlord_group)
            login(request, user)
            return redirect("/")
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/landlord_register.html', {'form': form})

def regular_signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            regular_group, _ = Group.objects.get_or_create(name="Regular")
            user.groups.add(regular_group)
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/regular_register.html", {'form': form})


            


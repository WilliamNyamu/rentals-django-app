from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser
# Create your views here.


def index(request):
    return render(request, 'accounts/base.html')

def regular(request):
    return HttpResponse("Regular page sanity checks")

def landlord(request):
    return HttpResponse("Landlord page sanity checks")



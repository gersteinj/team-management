from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime

from .forms import PersonForm

# Create your views here.
def index(request):
    return HttpResponse("Hi!")

def scan(request):
    return HttpResponse("You'll scan in/out here")

def new_person(request):
    form = PersonForm()    
    return render(request, 'attendance/edit_person.html', {'form': form})
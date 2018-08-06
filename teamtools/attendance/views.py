from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    return HttpResponse("Hi!")

def scan(request):
    return HttpResponse("You'll scan in/out here")

def add_member(request):
    return HttpResponse("You'll add yourself here")
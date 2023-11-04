from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "index.html") #HttpResponse("<h1> Le blog </h1>")
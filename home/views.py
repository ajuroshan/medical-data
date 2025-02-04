from django.shortcuts import render
from django.http import HttpResponse  # Corrected import

# Create your views here.

def home(request):
    return render(request,template_name="index.html")

def hello(request):
    
    return render(request,template_name="hello.html")

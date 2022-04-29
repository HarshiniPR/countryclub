from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def mr(request):
    return render(request, 'mr.html')

def reciprocals(request):
    return render(request, 'reciprocals.html')

def signup(request):
    return render(request, 'signup.html')
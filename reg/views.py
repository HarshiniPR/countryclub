from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth


def register(request):
    if request.method == 'POST':
        membership_payment_id = request.POST['mpi']
        membership_payment_amount = request.POST['mpa']
        membership_type = request.POST['mt']
        email = request.POST['email']
        name = request.POST['name']
        phone = request.POST['phone']
        date_of_birth = request.POST['dateOB']
        password1 = request.POST['pwd']
        password2 = request.POST['cpwd']
        user = User.objects.create_user(username=name, email=email)
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('Userhome.html')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login.html')
    else:
        return render(request, 'login.html')
# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from TimeSheetApp.models import *

def index(request):
    return render(request, 'register/index.html')

def login(request):
    return render(request, 'register/login.html')

def register(request):
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=request.POST['password'], email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    return redirect('/success')


def loginAction(request):
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        if request.POST['login_password'] == user.password:
            request.session['id'] = user.id
            return redirect('/success')
    return redirect('/login')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'register/success.html', context)
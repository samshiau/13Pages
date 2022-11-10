from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *

def tagFilter(request):
    products = product.objects.all()
    #if request.method == 'POST':



def index(request):
    # get products from database
    products = product.objects.all()
    if request.method == 'POST':
        search = request.POST['searchText']
        products = product.objects.filter(productName__icontains=search)
        return render(request, 'index.html', {'products': products})
    else:
        return render(request, 'index.html', {'products': products})

def login(request):
    return render(request, 'login.html')

def cart(request):
    return render(request, 'cart.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # check if the passwords match
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            else: # new user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('index')
        else: # incorrect password
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    
    else: # GET request
        return render(request, 'register.html')
    
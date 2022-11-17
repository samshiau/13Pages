from django.contrib import messages
from django.shortcuts import render, redirect

from .models import *


def index(request):
    products = product.objects.all()
    filter_tags = filter_tag.objects.all()

    if request.method == 'POST':
        search = request.POST['searchText']
        products = product.objects.filter(productName__icontains=search)
    elif request.method == 'GET':
        tagFilter = request.GET.get('item_filter')

        try:
            product_filter_tag = filter_tag.objects.get(tagName=tagFilter)
            products = product_filter_tag.products.all()
        except:
            print("Error: No filter tag found")
            pass

    return render(request, 'index.html', {'products': products, 'filter_tags': filter_tags})


def login(request):
    if request.method == 'POST':
        if request.POST['email'] and request.POST['password'] != None:
            email = str(request.POST['email']).strip().lower()
            password = request.POST['password']

            if User.objects.filter(email=email).exists():
                print(User.objects.filter(password=password).exists())
                return redirect('index')

            messages.info(request, 'Account does not exists')
            return redirect('register')

    return render(request, 'login.html')


def cart(request):
    return render(request, 'cart.html')


def register(request):
    if request.method == 'POST':
        username = str(request.POST['username']).strip()
        email = str(request.POST['email']).strip().lower()
        password = str(request.POST['password']).strip()
        confirm_password = str(request.POST['confirm_password']).strip()

        # check if the passwords match
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            else:  # new user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('index')
        else:  # incorrect password
            messages.info(request, 'Passwords do not match')
            return redirect('register')

    else:  # GET request
        return render(request, 'register.html')

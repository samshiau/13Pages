from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Item, Book


def index(request):
    # get data from database
    items = Item.objects.all()
    books = Book.objects.all()
    
    # sending the data to the template
    return render(request, 'index.html', {'items': items, 'books': books})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

    return render(request, 'register.html')
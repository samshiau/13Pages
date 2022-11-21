from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.sessions.models import Session

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


# add to cart
def add_to_cart(request):
    global length
    get_product = product.objects.filter(productName=request.GET['name']).values()[0]
    cart_p = dict()
    cart_p[str(request.GET['name'])] = {
        'ProductName': get_product['productName'],
        'price': str(get_product['productPrice']),
        'qty': 1
    }

    if 'cartdata' in request.session:
        if str(request.GET['name']) in request.session['cartdata']:
            cart_data = request.session['cartdata']

            cart_data[str(request.GET['name'])]['qty'] += 1
            cart_data.update(cart_data)
            request.session['cartdata'] = cart_data
        else:
            cart_data = request.session['cartdata']
            cart_data.update(cart_p)
            request.session['cartdata'] = cart_data
    else:
        request.session['cartdata'] = cart_p

    return JsonResponse({'data': request.session['cartdata'], 'totalitems': len(request.session['cartdata'])})


# Delete Cart Item
def delete_cart_item(request):
    product_name = str(request.GET['name'])
    if 'cartdata' in request.session:
        if str(request.GET['name']) in request.session['cartdata']:
            cart_data = request.session['cartdata']
            del request.session['cartdata'][product_name]
            request.session['cartdata'] = cart_data

    total_amount = 0.0
    for p_name, item in request.session['cartdata'].items():
        total_amount += int(item['qty']) * float(item['price']) * 1.0825

    total_amount = "{:.2f}".format(total_amount)
    t = render_to_string('cart-list.html',
                         {'cart_data': request.session['cartdata'], 'totalitems': len(request.session['cartdata']),
                          'total_amnt': total_amount})
    return JsonResponse({'data': t, 'totalitems': len(request.session['cartdata'])})


def cart(request):
    total_amount = 0.0
    for p_name, item in request.session['cartdata'].items():
        total_amount += int(item['qty']) * float(item['price']) * 1.0825

    total_amount = "{:.2f}".format(total_amount)

    return render(request, 'cart.html',
                  {'cart_data': request.session['cartdata'], 'totalitems': len(request.session['cartdata']),
                   'total_amnt': total_amount})


def checkout_cart_items(request):
    product_name = list()
    for p_name, item in request.session['cartdata'].items():
        product_name.append(p_name)

    if 'cartdata' in request.session:
        for name in product_name:
            cart_data = request.session['cartdata']
            del request.session['cartdata'][name]
            request.session['cartdata'] = cart_data

    total_amount = 0.0
    for p_name, item in request.session['cartdata'].items():
        total_amount += int(item['qty']) * float(item['price']) * 1.0825

    total_amount = "{:.2f}".format(total_amount)
    t = render_to_string('cart-list.html',
                         {'cart_data': request.session['cartdata'], 'totalitems': len(request.session['cartdata']),
                          'total_amnt': total_amount})
    return JsonResponse({'data': t})


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

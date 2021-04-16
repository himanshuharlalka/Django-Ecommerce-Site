
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

from django.http import JsonResponse
import json
import datetime
from .models import *
from django.views.generic import ListView


def user(request, user_id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

        favorite, created = Favorite.objects.get_or_create(
            customer=customer)
        favoriteitems = favorite.favoriteitem_set.all()
        favoriteitemsid = [item.product.id for item in favoriteitems]
        context = {'cartItems': cartItems,
                   'customer': customer, 'favoriteitems': favoriteitems,  'favoriteitemsid': favoriteitemsid}
    return render(request, 'store/user.html', context)


def product(request, product_id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        product = Product.objects.get(id=product_id)
        print(product.tags)
        sim_products = [item for item in Product.objects.all() if any(
            tag in item.tags for tag in product.tags)]
        favorite, created = Favorite.objects.get_or_create(
            customer=customer)
        favoriteitems = favorite.favoriteitem_set.all()
        favoriteitemsid = [item.product.id for item in favoriteitems]
        context = {"sim_products": sim_products,
                   "product": product, 'cartItems': cartItems,  'favoriteitemsid': favoriteitemsid}

        print(product)
        return render(request, 'store/product.html', context)

    else:
        product = Product.objects.get(id=product_id)
        context = {"product": product}
    return render(request, 'store/product.html', context)


def search(request):
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        search_result = Product.objects.all().filter(tags__icontains=search_term)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        products = Product.objects.all()
        favorite, created = Favorite.objects.get_or_create(
            customer=customer)
        favoriteitems = favorite.favoriteitem_set.all()
        favoriteitemsid = [item.product.id for item in favoriteitems]
        context = {'products': products, 'search_result': search_result,
                   'search_term': search_term, 'cartItems': cartItems}
    else:
        products = Product.objects.all()
        context = {'products': products, 'search_result': search_result,
                   'search_term': search_term,  'favoriteitemsid': favoriteitemsid}

    return render(request, 'store/search.html', context)


def fashion(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        products = Product.objects.all()
        favorite, created = Favorite.objects.get_or_create(
            customer=customer)
        favoriteitems = favorite.favoriteitem_set.all()
        favoriteitemsid = [item.product.id for item in favoriteitems]
        context = {'products': products, 'cartItems': cartItems,
                   'favoriteitemsid': favoriteitemsid}
    else:
        products = Product.objects.all()
        context = {'products': products}

    return render(request, 'store/fashion.html', context)


def books(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        products = Product.objects.all()
        favorite, created = Favorite.objects.get_or_create(
            customer=customer)
        favoriteitems = favorite.favoriteitem_set.all()
        favoriteitemsid = [item.product.id for item in favoriteitems]
        context = {'products': products, 'cartItems': cartItems,
                   'favoriteitemsid': favoriteitemsid}

    else:
        products = Product.objects.all()
        context = {'products': products}
    return render(request, 'store/books.html', context)


def electronics(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        products = Product.objects.all()
        favorite, created = Favorite.objects.get_or_create(
            customer=customer)
        favoriteitems = favorite.favoriteitem_set.all()
        favoriteitemsid = [item.product.id for item in favoriteitems]
        context = {'products': products, 'cartItems': cartItems,
                   'favoriteitemsid': favoriteitemsid}
    else:
        products = Product.objects.all()
        context = {'products': products}

    return render(request, 'store/electronics.html', context)


def accessories(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        products = Product.objects.all()
        favorite, created = Favorite.objects.get_or_create(
            customer=customer)
        favoriteitems = favorite.favoriteitem_set.all()
        favoriteitemsid = [item.product.id for item in favoriteitems]
        context = {'products': products, 'cartItems': cartItems,
                   'favoriteitemsid': favoriteitemsid}
    else:
        products = Product.objects.all()
        context = {'products': products}

    return render(request, 'store/accessories.html', context)


def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        favorite, created = Favorite.objects.get_or_create(
            customer=customer)
        favoriteitems = favorite.favoriteitem_set.all()
        favoriteitemsid = [item.product.id for item in favoriteitems]
    else:
        # Create empty cart for now for non-logged in user
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems,
               'favoriteitemsid': favoriteitemsid}
    return render(request, 'store/store.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        # Create empty cart for now for non-logged in user
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
        return redirect('login')

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        # Create empty cart for now for non-logged in user
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )
    else:
        print('User is not logged in')

    return JsonResponse('Payment submitted..', safe=False)


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect("register")
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=firstname, last_name=lastname)
                customer, created = Customer.objects.get_or_create(
                    user=user)
                print('user created')
                return redirect("login")
        else:
            messages.info(request, 'Password not matching..')
            return redirect("register")
        return redirect('/')
    else:
        return render(request, "store/register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:

        return render(request, "store/login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def history(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        orders = Order.objects.filter(
            customer=customer, complete=True)
        orderItems = OrderItem.objects.all()
        # items = order.orderitem_set.all()
        # cartItems = order.get_cart_items
    else:
        # Create empty cart for now for non-logged in user
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
        return redirect('login')

    # context = {'items': items, 'order': order, 'cartItems': cartItems}
    context = {'orders': orders, 'orderItems': orderItems}
    return render(request, 'store/history.html', context)


def updateFav(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    favorite, created = Favorite.objects.get_or_create(
        customer=customer)

    favoriteItem, created = FavoriteItem.objects.get_or_create(
        favorite=favorite, product=product)

    if action == 'add-fav':
        favoriteItem.save()
    elif action == 'remove-fav':
        favoriteItem.delete()

    return JsonResponse('Fav item was updated', safe=False)

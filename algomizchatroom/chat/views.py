from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Message, Category, User, Customer, Cart, Product, Order, OrderItem 
from chat.forms import ProductForm
from django.db.models import Q 
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ProductForm, UserForm, MyUserCreationForm



# Create your views here.

def loginpage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')
      
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')

    
    return render(request, 'login_register.html', {'page':page})

def logoutuser(request):
    logout(request)
    return redirect('home')

def registerpage(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
           user = form.save(commit=False)
           user.username = user.username.lower()
           user.save()
           login(request, user)
           return redirect('home')
    messages.error(request, 'An error occured during registration')
 
    return render(request, 'login_register.html',{'form':form })

def home(request):
    q = request.GET.get('q') if request.GET.get('q')!= None else ''
    products = Product.objects.filter(
        Q(category__name__icontains=q)|
        Q(name__icontains=q)|
        Q(description__icontains=q)
    )

    product_count = products.count()
    categories = Category.objects.all()
    product_messages = Message.objects.filter(Q(product__category__name__icontains=q))
    context = {'products': products, 'categories':categories, 'product_count':product_count, 'product_messages':product_messages}
    return render(request, 'home.html', context) 
 
def product(request,pk):
    product = Product.objects.get(id=pk)
    product_messages = product.message_set.all().order_by('-created')
    if request.method == 'POST':
        Message.objects.create(
        user=request.user,
        product=product,
        body=request.POST.get('body')
        )
        product.participants.add(request.user)
        return redirect('product', pk=product.id)
    context = {'product':product, 'product_messages':product_messages}
    return render(request, 'product.html', context)

def userprofile(request,pk):
    user = User.objects.get(id=pk)
    products = user.product_set.all()
    categories = Category.objects.all()
    product_messages = user.message_set.all()
    context = {'user':user, 'products':products, 'categories':categories, 'product_messages':product_messages}
    return render(request, 'profile.html', context)

def deletemessage(request,pk):
    message = Message.objects.get(id=pk)
    
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    
    return render(request, 'deleteform.html', {'obj':message})

@login_required(login_url='login')
def updateUser(request):
    user =request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('userprofile', pk=user.id)
    return render(request, 'update-user.html', {'form':form})

def categorypage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    categories= Category.objects.filter(Q(name__icontains=q))
    context = {'categories':categories}
    return render(request, 'category.html', context)

def activitypage(request):
    room_messages = Message.objects.all()
    return render(request, 'activity.html', {'room_messages':room_messages})

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'home.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        print(customer)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        
    context = {'items':items, 'order': order}
    return render(request, 'store/cart.html', context)

@login_required(redirect_field_name='logs')
def add_cart(request, id):
    if request.user:
        if request.method == 'POST':
            user = request.user
            item = Product.objects.get(pk=id)
            qnty =  request.POST.get('qty')
            carts = Cart(customer=user, product = item, qty = qnty, counter = '0')
            carts.save()
            products = Cart.objects.all()
            return render(request, 'cart.html', {'products':products})
        else:
            return render(request, 'home.html')


def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)
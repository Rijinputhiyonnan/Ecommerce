


from django.contrib.auth.models import User


from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import SignInForm
from .models import Category

from django.shortcuts import render, redirect, get_object_or_404

from .forms import CategoryForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .forms import ProductForm
from django.contrib.auth.decorators import user_passes_test

from .models import Customer
from django.contrib.auth.views import LoginView




from django.views.decorators.http import require_POST
from .models import Product, Cart, CartItem
















def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    is_admin = request.user.is_authenticated and request.user.is_staff
    return render(request, 'home.html', {'products': products, 'categories': categories, 'is_admin': is_admin})



from .forms import CustomerSignUpForm

def customer_signup(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer = Customer.objects.create(user=user, phone=form.cleaned_data['phone'])
            return redirect('signin')
    else:
        form = CustomerSignUpForm()

    # Add your additional context here
    products = Product.objects.all()
    categories = Category.objects.all()
    is_admin = request.user.is_authenticated and request.user.is_staff
    context = {
        'form': form,
        'products': products,
        'categories': categories,
        'is_admin': is_admin
    }

    return render(request, 'customer_signup.html', context)



def signin(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Incorrect username or password')
                print(messages)  # Add this line
    else:
        form = SignInForm()
    products = Product.objects.all()
    categories = Category.objects.all()
    is_admin = request.user.is_authenticated and request.user.is_staff
    context = {
        'form': form,
        'products': products,
        'categories': categories,
        'is_admin': is_admin
    }
    return render(request, 'signin.html', {'form': form, **context})




from django.contrib.auth import logout

def signout(request):
    logout(request)
    return redirect('home')



def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    products = Product.objects.all()
    categories = Category.objects.all()
    is_admin = request.user.is_authenticated and request.user.is_staff
    context = {
        'form': form,
        'products': products,
        'categories': categories,
        'is_admin': is_admin
    }
    return render(request, 'add_category.html', {'form': form, **context })


@login_required
def category_list(request):
    categories = Category.objects.all()
    print(categories)  # Add this line to debug
    products = Product.objects.all()
    categories = Category.objects.all()
    is_admin = request.user.is_authenticated and request.user.is_staff
    context = {
        
        'products': products,
        'categories': categories,
        'is_admin': is_admin
    }
    return render(request, 'category_list.html', {'categories': categories, **context})


@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_edit.html', {'form': form})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        if request.is_ajax():
            return JsonResponse({'success': True})
        else:
            return redirect('category_list')
    return render(request, 'category_delete.html', {'category': category})







def customer_list(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'customer_list.html', context)





def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_add.html', {'form': form})
# views.py
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    products = Product.objects.all()
    categories = Category.objects.all()
    is_admin = request.user.is_authenticated and request.user.is_staff
    context = {
        
        'products': products,
        'categories': categories,
        'is_admin': is_admin
    }
    return render(request, 'product_list.html', {'products': products,**context})


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_edit.html', {'form': form})

@require_POST
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')

from django.shortcuts import render
from .models import Cart


@login_required
def cart_detail(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = None
    products = Product.objects.all()
    categories = Category.objects.all()
    is_admin = request.user.is_authenticated and request.user.is_staff
    context = {
        
        'products': products,
        'categories': categories,
        'is_admin': is_admin
    }
    return render(request, 'cart_detail.html', {'cart': cart, **context})
from django.contrib.auth.decorators import login_required
@require_POST
@login_required
def cart_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart, created = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    item.quantity += 1
    item.save()

    if not request.user.is_authenticated:
        return redirect('signin', {'product_pk': pk})

    return redirect('home')



from django.shortcuts import render, redirect
from .models import CartItem


@require_POST
def update_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    quantity = request.POST.get('quantity')
    cart_item.quantity = int(quantity)
    cart_item.save()
    return redirect('cart_detail')

def edit_cart_item(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    return render(request, 'edit_cart_item.html', {'cart_item': cart_item})



@require_POST
def cart_remove(request, pk):
    item = get_object_or_404(CartItem, pk=pk)
    item.delete()
    return redirect('cart_detail')


def cart_checkout(request):
    # Your view logic here
    return render(request, 'cart_checkout.html')


@login_required
def customer_profile(request):
    customer = request.user.customer
    
    products = Product.objects.all()
    categories = Category.objects.all()
    is_admin = request.user.is_authenticated and request.user.is_staff
    context = {
        'customer': customer,
        'products': products,
        'categories': categories,
        'is_admin': is_admin
    }
    return render(request, 'customer_profile.html', context)

@login_required
def customer_update(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']

        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        customer = user.customer
        customer.phone = phone
        customer.save()

        messages.success(request, 'Your profile has been updated.')
    return redirect('customer_profile')


@user_passes_test(lambda u: u.is_superuser)
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    user = customer.user
    user.delete()
    return redirect('customer_list')



from .models import Category, Product

def product_details(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    
    
    return render(request, 'product_details.html', {'category': category, 'products': products})


from django.contrib.auth.decorators import login_required

@login_required
def customer_profile_delete(request, pk):
    request.user.delete()
    logout(request)
    return redirect('home')


def base(request):
     products = Product.objects.all()
     categories = Category.objects.all()
     is_admin = request.user.is_authenticated and request.user.is_staff
     return render(request, 'base.html', {'products': products, 'categories': categories, 'is_admin': is_admin})
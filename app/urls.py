"""
URL configuration for ec project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from app import views
from .views import *




urlpatterns = [
    path("",views.home,name="home"),
    path('signup/', customer_signup, name='customer_signup'),
    path('signin/', views.signin, name='signin'),
    path('signin/<int:product_pk>/', views.signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('add_category/', add_category, name='add_category'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('customers/', views.customer_list, name='customer_list'),
    
    path('products/add/', views.product_add, name='product_add'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('cart/add/<int:pk>/', views.cart_add, name='cart_add'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.cart_checkout, name='cart_checkout'),
    
    
    path('update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('edit/<int:item_id>/', views.edit_cart_item, name='edit_cart_item'),
    

    path('cart/remove/<int:pk>/', views.cart_remove, name='cart_remove'),
    # Your other URL patterns
    path('accounts/', include('django.contrib.auth.urls')),
    path('signin/<int:product_pk>/', views.signin, name='signin'),
    
    path('signin/<int:product_pk>/', views.signin, name='signin'),
    path('customer/profile/', views.customer_profile, name='customer_profile'),
    
    path('customer/update/', views.customer_update, name='customer_update'),
    
    path('categories/', views.category_list, name='category_list'),
    path('product-details/<int:category_id>/', views.product_details, name='product_details'),
    path('customer/delete/<int:pk>/', views.customer_profile_delete, name='customer_profile_delete'),
    
    path('customer/<int:customer_id>/delete/', delete_customer, name='delete_customer'),
    path('base/', views.base, name='base'),
    
]





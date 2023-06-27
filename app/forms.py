from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer

class CustomerSignUpForm(UserCreationForm):
    phone = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2')


from django import forms
from django.contrib.auth.forms import AuthenticationForm

class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].empty_label = "Select Category"
        
        
from django import forms
from .models import Category

class ProductCategoryForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

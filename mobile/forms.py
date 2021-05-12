from django import forms
from django.forms import ModelForm
from .models import Product,Order,Carts
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets={
            'product_name':forms.TextInput(attrs={'class':'text_inp', 'placeholder':'Product Name'}),
            'price': forms.NumberInput(attrs={'class': 'text_inp', 'placeholder': 'Price'}),
            'specifications': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Specifications'}),
            'image': forms.FileInput(attrs={'class': 'text_inp', 'placeholder': 'Image'}),

        }


# for registration
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'User Name'}),
            'email': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'text_inp', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'text_inp', 'placeholder': 'Confirm Password'})

        }


# LOGIN
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'User name'}),
                               label='UserName')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'text_inp', 'placeholder': 'Password'}),
                               label='Password')


#for email. but im not using it
# def authenticate(self,request,username=None,password=None):
# try:
##user=User.objects.get(email=username)
#  if user.check_password(password):
#     return user
# else:
#   return None
# except User.DoesNotExist:
#   return None
# def get_user(self,user_id):
#    try:
#       user=User.objects.get(pk=user_id)
#  except User.DoesNotExist:
#      return None


class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields=["user","product","address"]
        widgets = {
            'address': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Address'})
        }

class CartForm(ModelForm):
    class Meta:
        model = Carts
        fields="__all__"
        widgets = {
           'product': forms.Select(attrs={'class': 'text_inp'}),
            'quantity': forms.NumberInput(attrs={'class': 'text_inp'}),
            'user': forms.TextInput(attrs={'class': 'text_inp'}),
        }
        labels = {
            'quantity':'Quantity',
            'user': 'Username'
        }


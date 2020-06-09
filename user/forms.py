from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, FileInput, Select, ModelForm

from home.models import UserProfile
from product.models import Product


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username'  : TextInput(attrs={'id': 'username'}),
            'email'     : EmailInput(attrs={'id': 'email'}),
            'first_name': TextInput(attrs={'id': 'first_name'}),
            'last_name' : TextInput(attrs={'id': 'last_name'}),

        }

CITY = [
    ('Istabul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir'),
]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'image')
        widgets = {
            'phone'  : TextInput(attrs={'id': 'phone'}),
            'address': TextInput(attrs={'id': 'address'}),
            'city'   : Select(attrs={'id': 'city'}, choices=CITY),
            'country': TextInput(attrs={'id': 'country'}),
            'image'  : FileInput(attrs={'id': 'image'}),

        }

class UserProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'keywords', 'image', 'price', 'amount', 'detail', 'slug')
        widgets = {
            'image': FileInput(),
            'detail': CKEditorWidget(),

        }
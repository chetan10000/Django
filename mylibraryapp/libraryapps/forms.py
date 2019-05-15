from django import forms
from .models import Book

from .models import  Author
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.forms import widgets
from django.conf import settings



class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ['title','image' ,'description','author' ,'genre','language']
        

class AuthorForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = ['first_name' , 'last_name']
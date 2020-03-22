from django.contrib import admin
from .models import Status
from .forms import statusForm
# Register your models here.
class statusAdmin(admin.ModelAdmin):
    list_display = ['user' , '__str__' , 'image']
    form = statusForm

admin.site.register(Status , statusAdmin)
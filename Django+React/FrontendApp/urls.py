from django.urls import path
from . import views

urlpatterns =[
    path('',views.index),
    path('second/',views.second_index),
]

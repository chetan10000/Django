"""updateimage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from updateapp.views import jsonre_data,jsonView,JsonView2,SerializeView,Serializeall
from updateapp.api import views,urls
from django.conf.urls import url,include

urlpatterns = [
    url(r'^$',jsonre_data),
    
    url(r'^serialize/$',SerializeView.as_view()),
    
    url(r'^serialize/$',SerializeView.as_view()),
    
    url(r'^all/$',Serializeall.as_view()),
    url(r'^cbv1/$',jsonView.as_view()),
    url(r'^cbv2/$',JsonView2.as_view()),
    url(r'^api/updates/',include('updateapp.api.urls')),

    path('admin/', admin.site.urls),

]

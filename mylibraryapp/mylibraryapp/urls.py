"""mylibraryapp URL Configuration

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
from django.conf.urls import url
from libraryapps.views import Home,search,create,detail,remove,Edit
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^api/books/create$',create,name='create'),
    url(r'^api/books/$',Home,name='books'),
    url(r'^api/books/search/$',search,name='search'),
    url(r'^api/books/(?P<id>\d+)/$', detail, name='detail'), 
    url(r'^api/books/(?P<id>\d+)/remove$', remove, name='remove'), 
    url(r'^api/books/(?P<id>\d+)/edit$', Edit, name='edit'), 
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
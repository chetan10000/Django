"""myresume URL Configuration

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
from django.urls import path ,include 
from django.conf.urls import url ,static
import resume
from django.conf import settings
#from resume.views import index,detail #
from rest_framework import routers
from resume import views
from rest_framework.urlpatterns import format_suffix_patterns
from resume.views import classBaseView ,serializeDetailView ,serializeListView,ProfileView
import stusapp
import frontend


'''
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
   
    path('api/',include(router.urls)),
    path('admin/', admin.site.urls),

]
'''
urlpatterns= [ 
    path('react/',include('frontend.urls')),
    path('api/status/',include('stusapp.api.urls')),
    path('api/' , views.UserViewApi.as_view()),
    path('admin/', admin.site.urls),
    path('json/',classBaseView.as_view()),
    path('serialize/',serializeDetailView.as_view()),
    path('list/',serializeListView.as_view()),
    path('profile/',views.ProfileView.as_view()),
    path("socket/", include('django_socketio.urls')),
    path('client/',resume.views.client),
]

urlpatterns = format_suffix_patterns(urlpatterns)
if settings.DEBUG:
    urlpatterns = urlpatterns + static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
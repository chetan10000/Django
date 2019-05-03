from django.conf.urls import url
from myapp.api import views
from .views import  StatusApi        ###StatusListApi , StatusApi ,StatusCreateApi , StatusDetailsApi  ,StatusUpdateApi , StatusDeleteApi###


urlpatterns= [
    #url(r'^$',views.StatusListApi.as_view()),
    #url(r'^search/$',StatusApi.as_view()),
    url(r'^$',StatusApi.as_view()),
    #url(r'^create/$',StatusCreateApi.as_view()),

    #url(r'^(?P<id>\d+)/$',StatusDetailsApi.as_view()),
    #url(r'^(?P<id>\d+)/update/$',StatusUpdateApi.as_view()),
    #url(r'^(?P<id>\d+)/delete/$',StatusDeleteApi.as_view()),

]
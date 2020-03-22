from django.urls import path , include
from django.conf.urls import url
from .views import ListSearchView,StatusApiView , StatusAppCreate , StatusDetailView, StatusUpdateView , StatusDeleteView,StatusAllInOne

urlpatterns = [ 
    path('',StatusApiView.as_view()),
    path('create/',StatusAppCreate.as_view()),
    #url(r'^',ListSearchView.as_view()),

      #url('^(?P<id>.*)/update/$',ListUpdateView.as_view()),
       #url('^(?P<id>.*)/delete/$',ListDeleteView.as_view()),
    path('<int:id>',StatusDetailView.as_view()),
    path('<int:id>/update',StatusUpdateView.as_view()),
    path('<int:id>/delete',StatusDeleteView.as_view()),
    path('All/',StatusAllInOne.as_view()),
    



]
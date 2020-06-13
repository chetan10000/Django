from django.urls import path , include
from django.conf.urls import url
from .views import ListSearchView,StatusApiView , StatusAppCreate , StatusDetailView, StatusUpdateView , StatusDeleteView,StatusAllInOne,ProfileView,Add_Friend,Friend_requests,AcceptRequest,CancelRequest ,RemoveFriend

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
     path('add/',Add_Friend.as_view()),
    path('requests/',Friend_requests.as_view()),
    path('accept/',AcceptRequest.as_view()),
    path('cancel/',CancelRequest.as_view()),
    path('remove/',RemoveFriend.as_view()),
    path('profile/',ProfileView.as_view()),
    



]
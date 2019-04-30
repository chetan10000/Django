
from .views import (UpdateModelapi,UpdateModelListapi)
from django.conf.urls import url

urlpatterns = [
            url(r'^$',UpdateModelListapi.as_view()),
            url(r'^(?P<id>\d+)/$',UpdateModelapi.as_view()),
            ]
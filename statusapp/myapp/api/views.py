from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from myapp.models import Status
from myapp.serializer import StatusSerializers
from rest_framework import generics,mixins,permissions
from rest_framework.generics import ListAPIView
from django.shortcuts import get_object_or_404
import json
from myapp.serializer import StatusSerializers


def is_json(json_data):
    try:
        real_json = json.loads(json_data) 
        is_valid= True
    except:
        is_valid = False
    return is_valid


### this is just one api view ###

class StatusApi(mixins.CreateModelMixin,mixins.UpdateModelMixin , mixins.RetrieveModelMixin ,  mixins.DestroyModelMixin , generics.ListAPIView):### with mixins you can create a list object also so it add extra functionality in view ###
    permisson_classes       = [permissions.IsAuthenticatedOrReadOnly]### it will check that the person is authenticated or not ###
    #authentication_classes  = [SessionAuthentication] ### it will check how person is authenticated means by any tokens like JWT or Oauth or not
    serializer_class = StatusSerializers
    passed_id = None
    
      
    def get_queryset(self):
        request = self.request
        print(request.user) ### it will just give the user but you can modify user so we are going to make user only readable field ###
        qs = Status.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains = query) ### 2 underscore needed ##
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id',None) or self.passed_id
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj =get_object_or_404(queryset,id=passed_id)
            self.check_object_permissions(request, obj )
        return obj






    def post(self ,request , *args , **kwargs):
        return self.create(request, *args , **kwargs)

    def get(self , request , *args , **kwargs):
        url_pass_id = request.GET.get('id',None) 
        
        json_data={}
        body_ = request.body
        if is_json(body_):
            json_data=json.loads(request.body)

        new_pass_id= json_data.get('id',None)
        passed_id = url_pass_id or new_pass_id or None
        passed_id = self.passed_id
        if passed_id is not None:
            return self.retrieve(request , *args , **kwargs)
        return super().get(request, *args , **kwargs)

    def put(self , request, *args , **kwargs):
        return self.update(request, *args , **kwargs)

    def delete(self , request , *args , **kwargs):
        return self.destroy(request, *args , **kwargs)
    
    def perform_create(self , serializer):
        serializer.save(user=self.request.user)

 ### this are the views for generic api views and mixins ### 
     
"""
class StatusCreateApi(generics.CreateAPIView):
    permisson_classes       = []
    authentication_classes  = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializers
  


class StatusListApi(APIView):
    permisson_classes       = []
    authentication_classes  = []

    def get(self , request , format = None):
        qs = Status.objects.all()
        serializer=StatusSerializers(qs,many=True)
        return Response(serializer.data)

    def post(self , request , format = None):
        qs = Status.objects.all()
        serializer=StatusSerializers(qs,many=True)
        return Response(serializer.data)



class StatusApi( generics.ListAPIView): ### without mixins you can just get a list and search method ###
    permisson_classes       = []
    authentication_classes  = []
    serializer_class = StatusSerializers
      
    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains = query) ### 2 underscore needed ##
        return qs
"""
"""
class StatusApi(mixins.CreateModelMixin , generics.ListAPIView):### with mixins you can create a list object also so it add extra functionality in view ###
    permisson_classes       = []
    authentication_classes  = []
    serializer_class = StatusSerializers
      
    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains = query) ### 2 underscore needed ##
        return qs

    def post(self , request , *args , **kwargs):
        return self.create(request, *args , **kwargs)

class StatusCreateApi(generics.CreateAPIView):
    permisson_classes       = []
    authentication_classes  = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializers
  
    #def perform_create(self,serializer):


class StatusDetailsApi(generics.RetrieveAPIView):
    permisson_classes       = []
    authentication_classes  = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializers
    #lookup_field     = 'id' ### this is the field name you use as id in your url ### ###method 1 of output ##
    def get_object(self ,*args , **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id')
        return Status.objects.get(id=kw_id)   ### methos 2 of getting output ###
        

        
class StatusDetailsApi(mixins.DestroyModelMixin , mixins.UpdateModelMixin , generics.RetrieveAPIView):
    permisson_classes       = []
    authentication_classes  = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializers
    lookup_field     = 'id' ### this is the field name you use as id in your url ### ###method 1 of output ##
    
    def get_object(self ,*args , **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id')
        return Status.objects.get(id=kw_id)   ### methos 2 of getting output ###
     
    
       

    def put(self , request , *args , **kwargs): ### method 3 ###
        return self.update(request, *args , **kwargs)

    def delete(self , request , *args , **kwargs): 
        return self.destroy(request, *args , **kwargs)



class StatusUpdateApi(generics.UpdateAPIView):
    permisson_classes       = []
    authentication_classes  = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializers
    lookup_field = 'id'


class StatusDeleteApi(generics.DestroyAPIView):
    permisson_classes       = []
    authentication_classes  = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializers
    lookup_field = 'id'

"""
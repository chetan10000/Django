from rest_framework.views import APIView
from stusapp.models import Status
from .serializer import StatusSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,mixins
from django.shortcuts import get_object_or_404
import json
from rest_framework import permissions
from rest_framework import authentication

def is_json(json_data):
    try :
        real_json= json.loads(json_data)
        is_valid = True
    except:
        is_valid = False
    return is_valid
'''
class ListSearchView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]
    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs , many = True)
        return Response(serializer.data )

class StatusApiView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]
    serializer_class = StatusSerializer
    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(text=query)
        return qs

class StatusAppCreate(ListCreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class StatusDetailView(RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'

class StatusUpdateView(UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'

class StatusDeleteView(DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'
'''
class StatusAllInOne(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]
    serializer_class = StatusSerializer
    passed_id = None
    
    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(id__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id= request.GET.get('id',None) or self.passed_id
        query = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(query,id=passed_id) 
            self.check_object_permissions(request, obj)
        return obj

    def perform_destroy(self,instance):
        if instance is not None:
            return instance.delete()
        return None


    def get(self, request , *args, **kwargs):
        passed_id = self.request.GET.get('id',None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_body= json.loads(request.body)
            json_data_id = json_body.get('id', None)
            passed_id  = passed_id or json_data_id or None
            self.passed_id=passed_id
        if passed_id is not None:
            return self.retrieve(request, *args ,**kwargs)

        return super().get(request,*args,**kwargs)

   
        
    def post(self, request , *args, **kwargs):
        passed_id = self.request.GET.get('id',None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_body= json.loads(request.body)
            json_data_id = json_body.get('id', None)
            passed_id  = passed_id or json_data_id or None
            self.passed_id=passed_id
            return self.create(request,*args,**kwargs)
    
    def put(self , request , *args , **kwargs):
        passed_id = self.request.GET.get('id',None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_body= json.loads(request.body)
            json_data_id = json_body.get('id', None)
            passed_id  = passed_id or json_data_id or None
            self.passed_id = passed_id
            print(passed_id)
            return self.update(request , *args , **kwargs)

    def patch(self , request , *args , **kwargs):
        passed_id = self.request.GET.get('id',None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_body= json.loads(request.body)
            json_data_id = json_body.get('id', None)
            passed_id  = passed_id or json_data_id or None
            self.passed_id = passed_id
            return self.update(request , *args , **kwargs)

    def delete(self , request , *args , **kwargs):
        passed_id = self.request.GET.get('id',None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_body= json.loads(request.body)
            json_data_id = json_body.get('id', None)
            passed_id  = passed_id or json_data_id or None
            self.passed_id = passed_id
            return self.destroy(request , *args , **kwargs)

   
        



    


    



from rest_framework.views import APIView
from stusapp.models import Status
from .serializer import StatusSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,mixins
from django.shortcuts import get_object_or_404
import json
from rest_framework import permissions
from rest_framework import authentication
from django.contrib.auth.models import User
from django.views.generic import View
from django.core.serializers import serialize
from django.http import HttpResponse,JsonResponse
from friendship.models import Friend,FriendshipRequest
from django.contrib.auth import authenticate
import base64
def is_json(json_data):
    try :
        real_json= json.loads(json_data)
        is_valid = True
    except:
        is_valid = False
    return is_valid

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

class json_response(View):
    def get(self,request,*args,**kwargs):
        u = User.objects.all()
        data = serialize('json',u)
        return HttpResponse(data,content_type='application/json')

class Add_Friend(View):
    def post(self,request,*args ,**kwargs):
        json_loads = json.loads(request.body)
        username =json_loads.get('username')
        password = json_loads.get('password')
        json_id=int( json_loads.get('id'))
        u = User.objects.get(pk=json_id)
        user ={"user":u}
        #print(request.body)
        user = authenticate(username=username,password=password)
        if user:
            Friend.objects.add_friend(user,u,message='Hey! would you like to be friend?')
            friend_requests = Friend.objects.sent_requests(user = user)
            data  =serialize('json',friend_requests)
        
            return HttpResponse(data,content_type='application-json')


class Friend_requests(View):
    def get(self,request,*args,**kwargs):
        get_authorization=request.META['HTTP_AUTHORIZATION']
        slice_auth=get_authorization[5:]
        auth_decode= base64.b64decode(slice_auth)
        split_auth= auth_decode.decode("utf-8").split(':')
        username =split_auth[0]
        password = split_auth[1]
        user = authenticate(username=username,password=password)
        friend_requests  = [y.to_user for y in Friend.objects.sent_requests(user=user)]
        to_user= serialize('json',friend_requests,fields=('username'))
        Friends = Friend.objects.friends(user=user)
        friends_list = serialize('json',Friends,fields=('username'))

        '''
        u= User.objects.get(pk=1)
        for_Ex = [z.to_user for z in Friend.objects.sent_requests(user=user) if z.to_user==u]
        print(for_Ex)
        '''
        '''
        li=[]
        for x in json_user:
            id = x['fields']['to_user']
            users =[x.username for x in User.objects.filter(pk=id)]
            #datas = serialize('json',users,fields=('username'))
            li.append(users)
        '''
        
        print(Friends)
        got_requests =FriendshipRequest.objects.filter(to_user=user)
        requested_id= [x.from_user for x in got_requests.only('from_user')]
        json_requests = serialize('json',requested_id,fields=('username'))
        #print("requests",json_requests[0])
        #print(requested_id)
        #print(li)
        #print(json_requests)
        
        return JsonResponse([to_user,json_requests,friends_list],content_type='application-json',safe=False)

class AcceptRequest(View):
    def post(self,request,*args,**kwargs):
        json_loads = json.loads(request.body)
        username =json_loads.get('username')
        password = json_loads.get('password')
        json_id= json_loads.get('id')
        print(json_id)
        from_user= User.objects.get(pk=json_id)
    
        #print(request.body)
        user = authenticate(username=username,password=password)
        if user:
            #friendship_requests = [ x for x in FriendshipRequest.objects.filter(to_user=user) if x.from_user==u]
            friendship_request = FriendshipRequest.objects.get(to_user=user,from_user=from_user)
            friendship_request.accept()
            Friends = Friend.objects.all(user=user)
            friends_json = serialize('json',Friends)
            return HttpResponse(friends_json,content_type='application-json')
    


class RejectRequest(View):
    def post(self,request,*args,**kwargs):
        json_loads = json.loads(request.body)
        username =json_loads.get('username')
        password = json_loads.get('password')
        json_id=int( json_loads.get('id'))
        from_user= User.objects.get(pk=json_id)
    
        #print(request.body)
        user = authenticate(username=username,password=password)
        if user:
            #friendship_requests = [ x for x in FriendshipRequest.objects.filter(to_user=user) if x.from_user==u]
            friendship_request = FriendshipRequest.objects.get(to_user=user,from_user=from_user) 
            friendship_request.reject()
            Friends = Friend.objects.friends(user=user)
            friends_json = serialize('json',Friends)
            return HttpResponse(friends_json,content_type='application-json')

            
class CancelRequest(View):
    def post(self,request,*args,**kwargs):
        json_loads = json.loads(request.body)
        username =json_loads.get('username')
        password = json_loads.get('password')
        json_id=int( json_loads.get('id'))
        from_user= User.objects.get(pk=json_id)
    
        #print(request.body)
        user = authenticate(username=username,password=password)
        if user:
            #friendship_requests = [ x for x in FriendshipRequest.objects.filter(to_user=user) if x.from_user==u]
            friendship_request = FriendshipRequest.objects.get(from_user=user,to_user=json_id) 
            friendship_request.cancel()
            Friends = Friend.objects.sent_requests(user=user)
            friends_json = serialize('json',Friends)
            return HttpResponse(friends_json,content_type='application-json')



class RemoveFriend(View):
    def post(self,request,*args,**kwargs):
        json_loads = json.loads(request.body)
        username =json_loads.get('username')
        password = json_loads.get('password')
        json_id=int( json_loads.get('id'))
        from_user= User.objects.get(pk=json_id)
    
        #print(request.body)
        user = authenticate(username=username,password=password)
        if user:
            #friendship_requests = [ x for x in FriendshipRequest.objects.filter(to_user=user) if x.from_user==u]
            delete_friend = Friend.objects.remove_friend(to_user=user,from_user=from_user)
            Friends = Friend.objects.friends(user=user)
            friends_json = serialize('json',Friends)
            return HttpResponse(friends_json,content_type='application-json')







   
        



    


    



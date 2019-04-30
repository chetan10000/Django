from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.core.serializers import serialize
from .models import Update , UpdateManger
import json
from django.views.generic import View

# Create your views here.
#def deatails(request):#


def jsonre_data(request):
    data={
        "name":"chetan",
        "surname":"parmar"
    }
    json_data=json.dumps(data)
    return HttpResponse(json_data,content_type='application/json')


class jsonView(View):
    def get(self,request,*args,**kwargs):
        data={
        "name":"chetan",
        "surname":"parmar"
                }
        
        return JsonResponse(data)

class JsonResponseMixins(object):
    def render_json(self,context,**response_kwargs):
        return JsonResponse(self.get_data(context),**response_kwargs)

    def get_data(self,context):
        return context



class JsonView2(JsonResponseMixins,View):
    def get(self,request ,*args , **kwargs):
        data={
        "name":"chetan",
        "surname":"parmar"
                }
        
    
        return self.render_json(data)


class SerializeView(View):
    def get(self,request ,*args , **kwargs):
        obj=Update.objects.get(id=1)
        #data=serialize("json",[obj,],fields=("user","content"))
        #jason_data=data
        jason_data=obj.serialized()
        #data={
        #"user":obj.user.username,
        #"content":obj.content
               # }
       #jason_data=json.dumps(data)
        return HttpResponse(jason_data,content_type='application/java')
        
    
class Serializeall(View):
    def get(self,request ,*args , **kwargs):
        #obj=Update.objects.all()
        data=Update.objects.all().serialize()

        ##data=serialize("json",obj)##
        #data=serialize("json",obj,fields=("user","content"))
    

        ##data={
        ##"user":obj.user.username,##
        #"content":obj.content##
                #}##
                
        jason_data=json.dumps(data)
        return HttpResponse(jason_data,content_type='application/java')
        
    
       
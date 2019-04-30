from updateapp.models import Update , UpdateManger
from django.views.generic import View
from django.http import HttpResponse
from .mixins import CSRFExemptMixin,HttpResponseMixin
import json
from updateapp.forms import UpdateForm
from .utils import is_json

### create retrive update delete for single object ##
class UpdateModelapi(CSRFExemptMixin ,HttpResponseMixin, View):
    is_json =True
    def get_object(self,id=None):
        #try:
           # obj=Update.objects.get(id=id)
        #except Update.DoesNotExist:
           # obj = None
        
        qs=Update.objects.filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None
    



    def get(self,request , id , *args , **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_Data=json.dumps({"message":"update not available"})
            return self.render_to_response(error_Data , status = 404)
        json_data=obj.serialized()
        return self.render_to_response(json_data)
    

    def post(self,request , id ,*args , **kwargs):
        json_data= json.dumps({"message":"this method does not allowed"})
        return self.render_to_response(json_data , status = 403)

    
    def put(self,request ,id, *args , **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_Data=json.dumps({"message":"update not available"})
            return self.render_to_response(error_Data , status = 404)
        #print(request.POST)
        #print(request.data)
        print(request.body)
        valid_json=is_json(request.body)
        if not valid_json:
            error_data=json.dumps({"message":"data is not valid json type"})
            return self.render_to_response(error_data ,status=400)
        new_Data=json.loads(request.body)
        print(new_Data['content'])
        json_data=json.dumps({"message":" updated"})
        return self.render_to_response(json_data)



    def delete(self,request ,id, *args , **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_Data=json.dumps({"message":"you can not available"})
            return self.render_to_response(error_Data , status = 404)
        return HttpResponse({},content_type='application/json')
        json_data=json.dumps({"message":"deleted object"})
        return self.render_to_response(json_data)



## list api for entire model ##
class UpdateModelListapi(CSRFExemptMixin ,HttpResponseMixin, View):
    is_json = True

    def get(self,request , *args , **kwargs):
        obj = Update.objects.all()
        json_data=obj.serialize()
        return self.render_to_response(json_data,status=200)
    
    


    def post(self,request , *args , **kwargs):
        #print(request.POST)
        valid_json=is_json(request.body)
        if not valid_json:
            error_data=json.dumps({"message":"data is not valid json type"})
            return self.render_to_response(error_data ,status=400)
        new_data=json.loads(request.body)
        form =  UpdateForm(new_data)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data=obj.serialized()
            return self.render_to_response(obj_data,status=201)
        if form.errors:
            data=json.dumps(form.errors)
            return self.render_to_response(data,status=400)
        data = { "message" : "not allowed" }
        return self.render_to_response(data,status=400)
        



    
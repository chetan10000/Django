from django.db import models
from django.conf import settings
from django.core.serializers import serialize
import json
# Create your models here.
def upload_update_image(instance , filename):
    return "updates/{user}/{filename}".format(user=instance.user , filename=filename)
    

class Queryset(models.QuerySet):
    #def serialize(self):
        #qs=self
        #return serialize("json",qs,fields=('user','content','image'))

    #def serialize(self):
       # qs=self
       ## final_array=[]
        #for obj in qs:
        #    stuct = json.loads(obj.serialized())
          #  final_array.append(stuct)
        #return json.dumps(final_array)

    def serialize(self):
        qs=list(self.values("user","content","image"))
        return json.dumps(qs)

class UpdateManger(models.Manager):     ##serialize entire queryset##
    def get_queryset(self):
        return Queryset(self.model , using=self.db)



class Update(models.Model):
    user        =       models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content     =       models.TextField(blank=True, null=True)
    image       =       models.ImageField(upload_to=upload_update_image , blank=True , null=True)
    updated     =       models.DateTimeField(auto_now=True)
    timestamp   =       models.DateTimeField(auto_now_add=True)

    objects=UpdateManger()

    def __str__(self):
        return self.content or ""
    

    #def serialized(self):           ## this method serialize indivisual instance ##
      #  data  = serialize("json",[self], fields=('user','content','image'))
      #  stuct = json.loads(data)
      #  print(stuct)
      #  jdata = json.dumps(stuct[0]['fields'])  
      #  return (jdata)

    def serialized(self):
        try:
                image = self.image.url
        except:
                image = ""
         
        data={
            "id":self.id,
            "content":self.content,
              "user":self.user.id,
              "image":image

        }

      
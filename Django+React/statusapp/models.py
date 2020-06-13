from django.db import models
from django.conf import settings
from django.core.serializers import serialize

# Create your models here.
def upload_status_App(instance,filename):
    return "updates/{user}/{filename}".format(user=instance.user , filename=filename)

class GetQuerySet(models.QuerySet):
    pass

class StatusManager(models.Manager):
    def get_queryset(self):
        return GetQuerySet(self.model , using=self._db)


class Status(models.Model):
    user  = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete = models.CASCADE )
    text = models.TextField(null = True , blank=True)
    image = models.ImageField(upload_to=upload_status_App,null=True , blank = True)
    timestamp = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now_add= True)
    objects = StatusManager()


    def __str__(self):
        return str(self.text)[:50]

    class Meta:
        verbose_name = "Strus Post"
        verbose_name_plural = "Status Posts"

    '''
    def serialize(self):
        return serilize('json' , [self])
    '''
    

class Profile(models.Model):
    user  =     models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    image =   models.ImageField(upload_to=upload_status_App,null=True,blank=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
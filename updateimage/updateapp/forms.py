from django import forms
from .models import Update


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        fields= [ 
            'user',
            'content',
            'image'
        ]
    

    def clean(self ,*args , **kwargs):## this def clean() for cleaning data #
        data= self.cleaned_data
        
        content= data.get('content' , None)
        if content == "":
            content=None
        image=data.get("image",None)
        if content is None and image is None:
            raise forms.ValidationError('Content or Image is required')
        return super().clean(*args,**kwargs)
from .models import Status

from django import forms

class statusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields =['user' , 'text' ,'image']

    def clean(self , *args , **kwargs):
        data = self.cleaned_data
        text = data.get('text',None)
        if text == "":
            text  =None
        else:
            if len(text)>100:
                raise forms.ValidationError('too much text')
        image = data.get("image",None)
        if text is None and image is None:
            raise forms.ValidationError('Content and Image is required')
        return super().clean(*args,**kwargs)
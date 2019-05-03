from django import forms
from .models import Status

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields=[
            'user',
            'content',
            'image'
        ]

    def clean_content(self,*Args,**kwargs):
        content=self.cleaned_data.get('content')
        if len(content)>=200:
            raise forms.ValidationError("content length is more")
        return content

    def clean(self, *args , **kwargs):
        data=self.cleaned_data
        content=data.get('content',None)
        if content is None:
            content=None
        image=data.get('image',None)
        if image is None and content is None:
            raise forms.ValidationError('Content or image is required ')
        return super().clean(*args,**kwargs)



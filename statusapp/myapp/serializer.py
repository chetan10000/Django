from rest_framework import serializers
from .models import Status



class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields = ['user']

    def validate_content(self , value):
        if len(value)>100000:
            raise serializers.ValidationError("this is too way long")
        return value
    
    def validate(self , data):
        content = data.get("content" , None)
        if content == "":
            content = None
        image = data.get("image" , None)
        if content is None and image is None:
            raise serializers.ValidationError("content or image is required")
        return data


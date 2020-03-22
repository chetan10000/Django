from stusapp.models import Status
from rest_framework import serializers

class StatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Status
        fields = ['id','user','text','image']

    def validate_content(self, value):
        if len(value)>50:
            raise serializers.ValidationError("The conetent is too long ")
        return value
    
    def validate(self,data):
        content = data.get("text",None)
        if content == "":
            content is None
        image = data.get("image",None)
        if content is None and image is None:
            raise serializers.ValidationError("The content and image is required")
        return data
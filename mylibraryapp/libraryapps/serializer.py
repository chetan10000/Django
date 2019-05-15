from rest_framework import serializers
from .models import Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title','image' ,'description' ,'author','genre']
    
        depth = 1
        
class BookListSerializer(serializers.ListSerializer):
    child= BookSerializer()
    allow_null=True
    many=True
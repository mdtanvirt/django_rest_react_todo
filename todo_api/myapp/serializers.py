from rest_framework import serializers
from myapp.models import Contact

class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=30)

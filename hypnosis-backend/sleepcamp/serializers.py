from rest_framework_mongoengine.serializers import DynamicDocumentSerializer, DocumentSerializer, EmbeddedDocumentSerializer
from .models import UserProfileModel
from rest_framework import serializers

class UserProfileSerializer(DocumentSerializer):
    name = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    age = serializers.CharField(required=False)
    location = serializers.CharField(required=False)
    detail = serializers.CharField(required=False)

    class Meta:
        model = UserProfileModel
        fields = ('id', 'name', 'gender', 'age', 'location', 'detail')

from rest_framework import serializers
from .models import Upload
from users.serializers import UserSerializer

class FileSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    class Meta:
        model = Upload
        fields = ['name', 'object', 'created_at', 'updated_at', 'user']
        depth = 1
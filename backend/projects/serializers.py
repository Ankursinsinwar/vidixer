from rest_framework import serializers
from .models import Project
from users.models import User
from users.serializers import UserSerializer

class ProjectSerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only=True)
    editor = UserSerializer(read_only=True)
    editor_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role='editor'),
        source='editor',
        write_only=True,
        required=False
    )

    class Meta:
        model = Project
        fields = '__all__'

from rest_framework import serializers
<<<<<<< HEAD
from .models import User
=======
>>>>>>> 618fc8dde489b81878f88e55ee6a1552b94a7043
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'firstname', 'lastname']
        read_only_fields = ['id']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        validate_password(password, user)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', 'None')
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            validate_password(password, instance)
            instance.set_password(password)
        instance.save()
        return instance

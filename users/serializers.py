from rest_framework import serializers
from users import models

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.User
        fields = '__all__'
        extra_kwargs = {'last_login': {'write_only': True, 'required': False}
                        ,'is_superuser': {'write_only': True, 'required': False}
                        ,'is_staff': {'write_only': True, 'required': False}
                        ,'date_joined': {'write_only': True, 'required': False}
                        ,'groups': {'write_only': True, 'required': False}
                        ,'user_permissions': {'write_only': True, 'required': False}}
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups', 
                  'is_staff', 'is_superuser', 'is_active', 
                  'first_name', 'last_name']
        
        
class DoctorsSpecializationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorsSpecializations
        fields = ['__all__']
        

class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ['__all__']
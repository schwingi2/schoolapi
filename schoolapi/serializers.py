# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault
from .models import Sitznachbar



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}
################################################################

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
class SitznachbarSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source="user.username")#.username")  # new
    owner = serializers.ReadOnlyField(source="owner.username")
    #owner=self.request.user
    #owner= CurrentUserDefault()

    class Meta:
        model = Sitznachbar
        fields = ('id','pers_uuid','first_name','last_name','alias', 'rec_time', 'owner')
        

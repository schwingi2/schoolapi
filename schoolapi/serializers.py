# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault
from .models import Sitznachbar, Hobby



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
    
class HobbySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hobby
        fields = ('hobby_desc',)
        # if there is only one value in the fields section - you have to use comma operator
        # or you have to use fields='__all__'   

        #fields = ('hobby_desc', 'sitznachbar')

class SitznachbarSerializer(serializers.HyperlinkedModelSerializer):
    hobbies = HobbySerializer(many=True, read_only=True)
    #owner = serializers.ReadOnlyField(source="user.username")#.username")  # new
    owner = serializers.ReadOnlyField(source="owner.username")
    #owner=self.request.user
    #owner= CurrentUserDefault()

    class Meta:
        model = Sitznachbar
        fields = ('id','pers_uuid','first_name','last_name','alias','hobbies', 'rec_time', 'owner')
        def create(self, validated_data):
            hobbies_data = validated_data.pop('hobbies')
            sitznachbar = Sitznachbar.objects.create(**validated_data)
            for hobby_data in hobbies_data:
                Hobby.objects.create(sitznachbar=sitznachbar, **hobby_data)
            return sitznachbar
        



        

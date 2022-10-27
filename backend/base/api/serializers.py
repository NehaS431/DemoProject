from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('username', 'password', 'password2',
         'email', 'first_name', 'last_name','groups')
    # fields = '__all__'
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True},
      'groups':{'required':True}
    }
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs
  def create(self, validated_data):
    groups_data = validated_data.pop('groups')
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name'],
    )
    for group_data in groups_data:
        user.groups.add(group_data)
    user.set_password(validated_data['password'])
    user.save()
    return user


# class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
        }
    def validate_email(self, value):
        user = self.context['request'].user
        existing_mail=User.objects.filter(email=value).values_list('email',flat=True).first()
        if existing_mail!=value:
            if User.objects.exclude(pk=user.pk).filter(email=value).exists():
                raise serializers.ValidationError({"email": "This email is already in use."})
        return value


    def validate_username(self, value):
        user = self.context['request'].user
        existing_username=User.objects.filter(username=value).values_list('username',flat=True).first()
        # print(existing_username,value)
        if existing_username!=value:
            if User.objects.exclude(pk=user.pk).filter(username=value).exists():
                raise serializers.ValidationError({"username": "This username is already in use."})
        return value
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']
 
        instance.save()

        return instance

class GetUserListSerializer(serializers.ModelSerializer):
    class Meta:
        odel=User
        fields = ('username', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
        }
    # print(User.objects.filter(groups__name='user'))

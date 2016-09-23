from django.contrib.auth.models import User
from rest_framework import serializers
from pentagram.models import Photo, Comment, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'user', 'photo')

    def create(self, validated_data):
        photo = Photo.objects.create(**validated_data)
        photo.save()
        return photo


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'photo', 'user')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'photo', 'user')
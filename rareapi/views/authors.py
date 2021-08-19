"""View module for handling requests about categories"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from django.db.models import fields
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from rareapi.models import RareUser

class AuthorView(ViewSet):
    """[summary]

    Args:
        ViewSet ([type]): [description]
    """
    def list(self, request):
        """[summary]

        Args:
            request ([type]): [description]
        """
        authors = RareUser.objects.all()
        serializer = RareUserSerializer(authors, many=True, context={'request': request})
        return Response(serializer.data)

    def update(self, request, pk=None):
        """[summary]

        Args:
            request ([type]): [description]
            pk ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        author = RareUser.objects.get(pk=pk)

        author.user = request.data["user"]
        author.bio = request.data["bio"]

        author.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single author
        Returns:
            Response -- JSON serialized author instance
        """
        try:
            author = RareUser.objects.get(pk=pk)
            serializer = RareUserSerializer(author, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)



class UserSerializer(serializers.ModelSerializer):
    """[summary]

    Args:
        serializers ([type]): [description]
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_staff']


class RareUserSerializer(serializers.ModelSerializer):
    """[summary]

    Args:
        serializers ([type]): [description]
    """
    user = UserSerializer(many=False)

    class Meta:
        model = RareUser
        fields = ['id', 'user', 'bio', 'profile_image_url']
        depth = 1
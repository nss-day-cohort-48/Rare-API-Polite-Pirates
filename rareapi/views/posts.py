"""View module for handling requests about posts"""
from rareapi.models.rare_user import RareUser
from rareapi.models.post import Post
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.auth.models import User


class PostView(ViewSet):
    """Rare Posts"""

    def list(self, request):
        """Handle GET requests to posts resource

        Returns:
            Response -- JSON serialized list of posts
        """
        # Get all game records from the database
        posts = Post.objects.all()

        # FOREIGN KEYS
        category = self.request.query_params.get('category', None)
        if category is not None:
            posts = posts.filter(category__id=category)

        serializer = PostSerializer(
            posts, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single post

        Returns:
            Response -- JSON serialized post instance
        """
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users name"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class RareUserSerializer(serializers.ModelSerializer):
    """HI"""
    user = UserSerializer(many=False)
    class Meta:
        model = RareUser
        fields = ['user']


class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts

    Arguments:
        serializer type
    """
    rare_user = RareUserSerializer(many=False)

    class Meta:
        """HI"""
        model = Post
        fields = ('id', 'title', 'category', 'rare_user',
                  'publication_date', 'image_url', 'content', 'approved')
        depth = 1

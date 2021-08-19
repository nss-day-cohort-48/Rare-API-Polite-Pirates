from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rareapi.models import Comment, Post, RareUser

class CommentView(ViewSet):

    def list(self, request):
        """lists for comments"""
        comments = Comment.objects.all()
        serializer = CommentSerializer(
            comments, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):

        rareuser = RareUser.objects.get(user=request.auth.user)
        post = Post.objects.get(pk=request.data["post"])

        comment = Comment()
        comment.content = request.data["content"]
        comment.created_on = request.data["createdOn"]
        comment.author = rareuser
        comment.post = post

        try:
            comment.save()
            serializer = CommentSerializer(comment, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message},
            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            comment = Comment.objects.get(pk=pk)
            comment.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Comment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        comment = Comment.objects.get(pk=pk)

        comment.content = request.data["content"]
        # comment.created_on = request.data = request.data["createdOn"]
        # comment.auther = request.data["rareuser"]
        # comment.post = request.data["post"]
        comment.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)


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

class CommentSerializer(serializers.ModelSerializer):

    author = RareUserSerializer(many=False)

    class Meta:
        model = Comment
        fields = ( 'id', 'content', 'created_on', 'author', 'post' )

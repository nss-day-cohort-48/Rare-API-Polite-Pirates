"""View module for handling requests about game types"""
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rareapi.models import Tag


class TagView(ViewSet):
    """The view for the Tag model
    methods:
        list: returns a list of all Tags
        retrieve: returns a single game type based on id
    """

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized game instance
        """
        tag = Tag()
        tag.label = request.data["label"]

        try:
            tag.save()
            serializer = TagSerializer(
                tag, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk):
        """Retrieves a single Tag
        Args:
            request (Request): the request object
            pk (int): the id requested in the url
        Returns:
            Response: serialized tag object
        """
        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerializer(
                tag, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Gets all game types in the database
        Args:
            request (Request): the request object
        Returns:
            Response: serialized list of all game types
        """
        tags = Tag.objects.all()
        serializer = TagSerializer(
            tags, context={'request': request}, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """Handle PUT requests for a tag
        Returns:
            Response -- Empty body with 204 status code
        """
        tag = Tag.objects.get(pk=pk)

        tag.label = request.data["label"]
        tag.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single tag
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            tag = Tag.objects.get(pk=pk)
            tag.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Tag.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TagSerializer(serializers.ModelSerializer):
    """Tag model serializer returns __all__ fields
    """
    class Meta:
        model = Tag
        fields = '__all__'
        depth = 1

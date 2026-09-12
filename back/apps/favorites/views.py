from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Favorites
from .serializers import FavoritesSerializer

@api_view(["GET", "POST"])
def favorites(request):
    if request.method == "GET":
        model = Favorites.objects.all()
        serializer = FavoritesSerializer(model, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = FavoritesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PATCH", "DELETE"])
def favorites_details(request, favorites_id):
    try:
        favorites = Favorites.objects.get(id=favorites_id)
    except Favorites.DoesNotExist:
        return Response(
            {"detail": "Favorite not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        serializer = FavoritesSerializer(favorites)
        return Response(serializer.data)

    if request.method == "PATCH":
        serializer = FavoritesSerializer(
            favorites,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    if request.method == "DELETE":
        favorites.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

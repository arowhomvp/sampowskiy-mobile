from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Addresses
from .serializers import AddressesSerializer

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def addresses(request):
    if request.method == "GET":
        addresses = Addresses.objects.filter(user = request.user)
        serializer = AddressesSerializer(addresses, many = True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = AddressesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def addresses_details(request, addresses_id):
    try:
        addresses = Addresses.objects.get(id = addresses_id, user = request.user)
    except Addresses.DoesNotExist:
        return Response({"detail": "Address was not found"},status=status.HTTP_404_NOT_FOUND)
    if request.method == "PATCH":
        serializer = AddressesSerializer(addresses, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST
)
    if request.method == "DELETE":
        addresses.delete()
        return Response({"Address was deleted"}, status=status.HTTP_204_NO_CONTENT)
    if request.method == "GET":
       serializer = AddressesSerializer(addresses)
       return Response(serializer.data, status=status.HTTP_200_OK)

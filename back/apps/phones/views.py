from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Phones
from .serializers import PhonesSerializer

@api_view(["GET", "POST"])
def phones(request):
    if request.method == "GET":
        phones = Phones.objects.all()
        serializer = PhonesSerializer(phones, many = True)
        return Response(serializer.data) 
    if request.method == "POST":
        serializer = PhonesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(["DELETE", "PATCH"])
def phones_detail(request, phones_id):
    try:
        phones = Phones.objects.get(id=phones_id)
    except Phones.DoesNotExist:
        return Response(
            {"error": "Phone not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "PATCH":
        serializer = PhonesSerializer(
            phones,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    if request.method == "DELETE":
        phones.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




    

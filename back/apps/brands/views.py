from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Brands
from .serializers import BrandsSerializer


@api_view(["GET", "POST"])
def brands(request):
    if request.method == "GET":
        brands = Brands.objects.all()
        serializer = BrandsSerializer(brands, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = BrandsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["PATCH", "DELETE"])
def brands_detail(request, brands_id):
    try:
        brand = Brands.objects.get(id=brands_id)
    except Brands.DoesNotExist:
        return Response(
            {"error": "Brand not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "PATCH":
        serializer = BrandsSerializer(
            brand,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    if request.method == "DELETE":
        brand.delete()
        return Response({"Brand Deleted"},
            status=status.HTTP_204_NO_CONTENT)

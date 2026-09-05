from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Brands
from .serializers import BrandsSerializer


@api_view(["GET", "POST"])
def brands(request):
    if request.method == "GET":
      brands = Brands.objects.all()
      serializers = BrandsSerializer(brands, many=True)
      return Response(serializers.data)

    if request.method == "POST":
       serializers = BrandsSerializer(data = request.data)
       if serializers.is_valid():
          serializers.save
          return Response(
             serializers.data,
             status=status.HTTP_201_CREATED
          )
       else:
          return Response(
             serializers.errors,
             status=status.HTTP_400_BAD_REQUEST
          )

@api_view(["PATCH", "DELETE"])
def brands_detail(request, brands_id):
    try:
        Brands = Brands.objects.get(id=brands_id)
    except Brands.DoesNotExist:
        return Response(
            {"error": "Brand not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "PATCH":
       serializer = BrandsSerializer(brands, data = request.data, Partial = True)
       if serializer.is_valid:
          serializer.save()
          return Response(
             serializer.data
          )
       else:
          return Response(
             serializer.errors, 
             status=status.HTTP_400_BAD_REQUEST
          )

    if request.method == "DELETE":
       brands.delete()
       return Response(
          status=status.HTTP_200_OK
       )
       
    
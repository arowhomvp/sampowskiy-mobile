from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Carts, CartsItem
from .serializers import CartsSerializer, CartsItemSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def carts(request):

    if request.method == "GET":
        carts = Carts.objects.filter(user=request.user)
        serializer = CartsSerializer(carts, many=True)
        return Response(serializer.data)

    if request.method == "POST":
       serializer = CartsSerializer(data = request.data)
       if serializer.is_valid():
        serializer.save(user = request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

       
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def carts_details(request, carts_id):
   try:
      carts = Carts.objects.get(id = carts_id, user = request.user)
   except Carts.DoesNotExist:
      return Response({"Cart not found"}, status=status.HTTP_404_NOT_FOUND)
   
   if request.method == "GET":
        carts = Carts.objects.filter(user=request.user)
        serializer = CartsSerializer(carts, many=True)
        return Response(serializer.data)
   
   if request.method == "PATCH":
      serializer = CartsSerializer(carts, data = request.data, partial = True)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status = status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


   if request.method == "DELETE":
      carts.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(["GET", "PATCH", "DELETE"])
def items(request, item_id):
   try:
      item = CartsItem.objects.get(id = item_id)
   except CartsItem.DoesNotExist:
      return Response({"Item not found"}, status=status.HTTP_404_NOT_FOUND)

   if request.method == "GET":
      serializer = CartsItemSerializer(item, many = True)
      return Response(serializer.data)
   if request.method == "PATCH":
      serializer = CartsItemSerializer(item, data = request.data, partial = True)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_200_OK)
   if request.method == "DELETE":
      item.delete()
      return Response({"Item was deleted"}, status=status.HTTP_204_NO_CONTENT)
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import OrdersItem, Orders
from .serializers import OrdersItemSerializer, OrdersSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def orders(request):
    if request.method == "GET":
       orders = Orders.objects.filter(user = request.user)
       serializer = OrdersSerializer(orders, many=True)
       return Response(serializer.data)

    if request.method == "POST":
        serializer = OrdersSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "DELETE", "PATCH"])
@permission_classes([IsAuthenticated])
def orders_details(request, orders_id):
    try:
       orders = Orders.objects.get(id = orders_id, user = request.user)
    except Orders.DoesNotExist:
        return Response({"Order was not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "PATCH":
        serializer = OrdersSerializer(orders, request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        orders.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == "GET":
        orders = Orders.objects.get(id = orders_id, user = request.user)
        serializer = OrdersSerializer(orders)
        return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def orders_items(request, orders_id):

    if request.method == "GET":
        items = OrdersItem.objects.filter(
            order_id=orders_id,
            order__user=request.user
        )
        serializer = OrdersItemSerializer(items, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        try:
            order = Orders.objects.get(
                id=orders_id,
                user=request.user
            )
        except Orders.DoesNotExist:
            return Response(
                {"detail": "Order was not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = OrdersItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(order=order)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(["GET", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def orders_item_details(request, orders_id, item_id):

    try:
        item = OrdersItem.objects.get(
            id=item_id,
            order_id=orders_id,
            order__user=request.user
        )
    except OrdersItem.DoesNotExist:
        return Response(
            {"detail": "Order item was not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        serializer = OrdersItemSerializer(item)
        return Response(serializer.data)

    if request.method == "PATCH":
        serializer = OrdersItemSerializer(
            item,
            request.data,
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
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Notifications
from .serializers import NotificationsSerializer

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def notifications(request):
    if request.method == "GET":
        notifications = Notifications.objects.filter(user = request.user)
        serializer = NotificationsSerializer(notifications, many = True)
        return Response(serializer.data)
    if request.method == "POST":
        if not request.user.is_staff:
            return Response({"Only for administration"}, status=status.HTTP_403_FORBIDDEN)
        serializer = NotificationsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def notifications_details(request, notification_id):
    try:
        notifications = Notifications.objects.get(
            id = notification_id,
            user = request.user
            )
    except Notifications.DoesNotExist:
        return Response({"Notification not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = NotificationsSerializer(notifications)
    return Response(serializer.data)
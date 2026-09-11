from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Reviews
from .serializers import ReviewsSerializer


@api_view(["GET", "POST"])
def reviews(request):
    if request.method == "GET":
        reviews = Reviews.objects.all()
        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ReviewsSerializer(data=request.data)

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


@api_view(["GET", "PATCH", "DELETE"])
def reviews_detail(request, reviews_id):
    try:
        review = Reviews.objects.get(id=reviews_id)
    except Reviews.DoesNotExist:
        return Response(
            {"error": "Review not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        serializer = ReviewsSerializer(review)
        return Response(serializer.data)

    if request.method == "PATCH":
        serializer = ReviewsSerializer(
            review,
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
        review.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

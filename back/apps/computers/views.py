from django.shortcuts import render


def computers_page(request):
    render(request, "computers/computers.html")

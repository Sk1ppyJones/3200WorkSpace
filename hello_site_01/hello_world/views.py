from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def home_view(request):
    return HttpResponse("Hello World!")

def greeting_view(request, name):
    return HttpResponse(f"<h1>Hello {name.capitalize()}! Hope Your Day Is Good!</h1>")

def square_view(request, num):
    square = num*num
    return HttpResponse(f'<h1>The square of {num} is {square}</h1>')
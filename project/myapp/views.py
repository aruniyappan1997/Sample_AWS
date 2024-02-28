from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse(f"<h1>Hello 'Arun Iyappan', <br> AWS is Working with Django!</h1>")
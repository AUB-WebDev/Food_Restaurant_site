from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def viewIndex(request):
    return  render(request, 'index.html')
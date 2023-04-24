from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

import requests

# Create your views here.
def index(request):
    ...
    return render(request, 'index.html')

# def blog(request):
#     ...
#     return render(request, 'blog.html')

# def single_post(request):
#     ...
#     return render(request, 'singlepost.html')

def about(request):
    ...
    return render(request, 'about.html')

def contact(request):
    ...
    return render(request, 'contact.html')

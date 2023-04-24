from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

import requests

def index(request):
    """
    Get all index
    """
    return render(request, 'spacex/about.html')

def info(request):
    """
    Get all info
    """
    import requests
    url = "https://api.spacexdata.com/v3/info"
    payload={}
    files={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload, files=files)
    # print(response.json())
    return render(request, 'spacex/about.html', context=response.json())

def missions(request):
    """
    Get all missions
    """
    import requests
    url = "https://api.spacexdata.com/v3/missions/F3364BF"
    payload={}
    files={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload, files=files)
    # print(response.json())
    return render(request, 'spacex/missions.html', context=response.json())

def launches(request):
    """
    Get all capsules
    """
    import requests
    url = "https://api.spacexdata.com/v3/launches/67"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    return render(request, 'spacex/launches.html', context=response.json())

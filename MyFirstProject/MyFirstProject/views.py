from django.http import HttpResponse
from django.shortcuts import render
def aboutUs(request):
    return HttpResponse("This is the about us page of MyFirstProject")

def clientDetails(request,clientId):
    return HttpResponse(f"{clientId} details are fetched")

def homePage(request):
    data = {
        'message' : 'Welcome to  Django project...',
        'list' : ['1','2','3']
    }
    return render(request, 'home.html', data)
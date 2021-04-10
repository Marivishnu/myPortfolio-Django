from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def home(request):

    myprojects = Project.objects.all()

    return render(request, "MyPortfolio/home.html", {'projects': myprojects})

def details(request, pk):
    print("Pk is", pk, "*******************************************")
    detail = Project.objects.get(pk=pk)
    return render(request, "MyPortfolio/details.html", {'project': detail})

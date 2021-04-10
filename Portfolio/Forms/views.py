from django.shortcuts import render, redirect
from django.http import HttpResponse
from MyPortfolio.models import Project
from .forms import ProjectForm
from django.contrib import messages

# Create your views here.
def addProject(request):

    newProject = ProjectForm()

    if request.method == 'POST':
        newProject = ProjectForm(request.POST, request.FILES)
        if newProject.is_valid():
            newProject.save()
            messages.info(request, 'Project Added')
            return redirect("/")


    return render(request, "Forms/forms.html", {'project': newProject})

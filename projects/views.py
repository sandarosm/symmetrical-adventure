from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def project_main(request):
    return render(request, "projects/project.html")

def project_dete(request):
    return render(request, "projects/project_dete.html")

def project_dcse(request):
    return render(request, "projects/project_dcse.html")
'''
def project_dete16(request):
    return render(request, "projects/project_dete16.html")

def project_dcse16(request):
    return render(request, "projects/project_dcse16.html")

def project_dete17(request):
    return render(request, "projects/project_dete17.html")

def project_dcse17(request):
    return render(request, "projects/projects_dcse17.html")

'''

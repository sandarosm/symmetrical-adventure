from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.



def dcse_main(request):
    return render(request, "dcse/dcse.html")

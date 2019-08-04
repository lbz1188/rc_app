from django.shortcuts import render
from django.http import HttpResponse
from .models import Resort

# Create your views here.


def home(request):
    context = {
        "resorts": Resort.objects.all()
    }
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")

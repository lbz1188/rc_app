from django.shortcuts import render
from django.http import HttpResponse
from .models import Resort
from django.views.decorators.cache import cache_page
import random
import os
# Create your views here.
# def randstring(num_string):
#     randstr = "".join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], num_string))
#     os.rename("".join([os.getcwd(),"\dg_project\homepage\static\index.css"]),"".join([os.getcwd(), f"\dg_project\homepage\static\index?version={randstr}.css"] ))
#     return randstr

# randstring(5)

@cache_page(10)
def home(request): 
    context = {

        "resorts": Resort.objects.all()
    }
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")

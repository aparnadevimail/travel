from django.shortcuts import render
from django.http import HttpResponse

from .models import place, team


def demo(request):
    obj= place.objects.all()
    obje=team.objects.all()
    return render(request,"index.html",{'result':obj,'results':obje})

# def about(request):
#     return render(request,"about.html")

# Create your views here.

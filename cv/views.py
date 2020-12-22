from django.shortcuts import render
from .models import Work
# Create your views here.

def about(request):
    works = Work.objects.all()

    return render(request, "cv/about.html", {'works':works})

def cv(request):
    works = Work.objects.all()

    return render(request, "cv/cv.html", {'works':works})

def tech(request):

    return render(request, "cv/tech.html")
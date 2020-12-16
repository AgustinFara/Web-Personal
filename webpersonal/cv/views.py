from django.shortcuts import render
from .models import Work
# Create your views here.

def about(request):
    works = Work.objects.all()

    return render(request, "cv/about.html", {'works':works})
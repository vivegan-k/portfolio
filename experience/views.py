from django.shortcuts import render
from .models import Experience

# Create your views here.
def experience(request):
    exp = Experience.objects
    return render(request, 'experience/experience.html', {'experiences':exp})

def gallery(request):
    return render(request, 'experience/gallery.html')
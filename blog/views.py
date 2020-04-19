from django.shortcuts import render

# Create your views here.

def highlights(request):
    return render(request, 'blog/highlights.html')



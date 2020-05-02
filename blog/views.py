from django.shortcuts import render
#from django.shortcuts import get_object_or_404

# Create your views here.

def highlights(request):
    return render(request, 'blog/highlights.html')

def skillset(request):
    return render(request, 'blog/skillset.html')

#def detail(request, blog_id):
#    detailblog = get_object_or_404(Blog, pk=blog_id)
#    return render(request, 'blog/detail.html', {'blog':detailblog})

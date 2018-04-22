from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog

# Create your views here.
def index(request):
    # blog = Blog.objects.all()
    blog = Blog.objects.all().first()
    return render(request, 'blog.html', {'blog': blog})
    # return render(request, 'blog.html')
    # return HttpResponse("Blog's blog")

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog
import markdown

# Create your views here.
def index(request):
    # blog = Blog.objects.all()
    blog = Blog.objects.all().first()
    blog_content = markdown.markdown(blog.content)
    return render(request, 'blog.html', {'blog' : blog, 'blog_content': blog_content})
    # return render(request, 'blog.html')
    # return HttpResponse("Blog's blog")

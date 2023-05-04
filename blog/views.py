from django.shortcuts import render
from .models import Post

# Create your views here.

def blog(request):
    nombre_url = request.resolver_match.url_name
    posts = Post.objects.all()
    return render(request,'blog/blog.html',{'posts':posts,'nombre_url': nombre_url})

def noticia(request,post_id):
    nombre_url = request.resolver_match.url_name
    post = Post.objects.get(id=post_id)
    return render(request,'blog/noticia.html',{'nombre_url': nombre_url,'noticia':post})
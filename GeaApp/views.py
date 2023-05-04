from django.shortcuts import render
from .models import Seccion
from blog.models import Post

# Create your views here.

def index(request):
    nombre_url = request.resolver_match.url_name
    posts=Post.objects.all()
    secciones=Seccion.objects.all()
    return render(request,"index.html",{"posts":posts,"secciones":secciones,'nombre_url': nombre_url})
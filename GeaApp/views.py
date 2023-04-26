from django.shortcuts import render
from .models import Seccion
from blog.models import Post

# Create your views here.

def index(request):
    posts=Post.objects.all()
    secciones=Seccion.objects.all()
    return render(request,"index.html",{"posts":posts,"secciones":secciones})
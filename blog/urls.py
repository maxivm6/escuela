from django.urls import path
from .views import blog,noticia 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',blog,name="blog"),
    path('noticia/<post_id>',noticia,name='noticia')
]

urlpatterns += static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)
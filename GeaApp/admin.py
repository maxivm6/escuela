from django.contrib import admin
from .models import Seccion


# Register your models here.


    
class SeccionAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
     
    
admin.site.register(Seccion,SeccionAdmin)
from django.contrib import admin
from .models import TurModel, Image

# Register your models here.

class TurAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'klass', ]



admin.site.register(TurModel, TurAdmin)
admin.site.register(Image)
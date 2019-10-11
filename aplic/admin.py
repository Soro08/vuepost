

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class MyImageAdmin(admin.ModelAdmin):

    list_display = ('id', 'image')
    
def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.MyImage, MyImageAdmin)
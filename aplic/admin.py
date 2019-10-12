
from django.utils.safestring import mark_safe
# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class MyImageAdmin(admin.ModelAdmin):

    list_display = ('id', 'images', 'name', 'username', 'email', 'phone')
    def images(self, obj):

        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.image.url))
        


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.MyImage, MyImageAdmin)
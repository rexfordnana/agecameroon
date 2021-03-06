from django.contrib import admin
from . import models


class ImageInline(admin.StackedInline):
    model = models.Image


class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Post, PostAdmin)



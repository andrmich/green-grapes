from django.contrib import admin
from .models import Post
from modeltranslation.admin import TranslationAdmin

class PostAdmin(TranslationAdmin):
    pass


admin.site.register(Post, PostAdmin)
# Register your models here.

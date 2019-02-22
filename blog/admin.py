from django.contrib import admin
from .models import Post, Skill
from modeltranslation.admin import TranslationAdmin

class PostAdmin(TranslationAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Skill)
# Register your models here.

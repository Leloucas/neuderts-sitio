from django.contrib import admin
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin

class ModelAdmin(SummernoteModelAdmin):
    summer_note_fields = ('body',)


admin.site.register(Blog, ModelAdmin)

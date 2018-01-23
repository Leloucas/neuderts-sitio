from django.contrib import admin
from .models import Portfolio
from django_summernote.admin import SummernoteModelAdmin

class ModelAdmin(SummernoteModelAdmin): 
    summer_note_fields = ('body',)

admin.site.register(Portfolio, ModelAdmin)

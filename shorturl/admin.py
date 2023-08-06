from django.contrib import admin
from .models import Shortner
# Register your models here.
@admin.register(Shortner)
class ShortenerAdmin(admin.ModelAdmin):
    list_display = ['id', 'long_url', 'short_url', 'times_followed', 'created', 'last_accessed']
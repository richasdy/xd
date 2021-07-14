from django.contrib import admin
from .models import chart

class chartAdmin(admin.ModelAdmin):
    list_display = ('Country', 'Value')

admin.site.register(chart, chartAdmin);

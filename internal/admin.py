from django.contrib import admin
from .models import chart, streamgraph

@admin.register(chart)
class chartAdmin(admin.ModelAdmin):
    list_display = ('Country', 'Value')

@admin.register(streamgraph)
class streamgraphAdmin(admin.ModelAdmin):
    list_display = ('year', 'Amanda', 'Ashley', 'Betty', 'Deborah', 'Dorothy', 'Helen', 'Linda', 'Patricia')
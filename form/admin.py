from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import logs

# Register your models here.
@admin.register(logs)
class logAdmin(admin.ModelAdmin):
    list_display = ('Time', 'Name', 'Level', 'Message')
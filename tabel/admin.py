from tabel.models import tabel
from django.contrib import admin

# Register your models here.
@admin.register(tabel)
class tabelAdmin(admin.ModelAdmin):
    list_display = ('id', 'waktu', 'nama', 'level', 'pesan' )

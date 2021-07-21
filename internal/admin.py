from django.contrib import admin
from .models import chart, density, streamgraph
from .models import TableModel
from .models import UserLog

@admin.register(chart)
class chartAdmin(admin.ModelAdmin):
    list_display = ('Country', 'Value')

@admin.register(streamgraph)
class streamgraphAdmin(admin.ModelAdmin):
    list_display = ('year', 'Amanda', 'Ashley', 'Betty', 'Deborah', 'Dorothy', 'Helen', 'Linda', 'Patricia')

@admin.register(density)
class densityAdmin(admin.ModelAdmin):
    list_display = ('id','price')

@admin.register(TableModel)
class tableAdmin(admin.ModelAdmin):
    list_display = ('username','email','password')

@admin.register(UserLog)
class UserLogAdmin(admin.ModelAdmin):
    list_display = ['activity', 'username', 'ip', 'timestamp']
    list_filter = ['activity',]


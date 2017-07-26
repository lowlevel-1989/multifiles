from django.contrib import admin
from .models import File, Ticket

class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'file')

admin.site.register(File, FileAdmin)
admin.site.register(Ticket)

from django.contrib import admin
from .models         import Work
from .models         import Client
# Register your models here.

class WorkAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Work)

class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Client)

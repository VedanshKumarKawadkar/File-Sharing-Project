from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class UserDetailsAdmin(UserAdmin):
    list_display = ("email", "username", "name", "date_joined", "received_files_keys")
    search_fields = ("email", "username")
    readonly_fields = ("date_joined", "received_files_keys")
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(UserDetails, UserDetailsAdmin)
admin.site.register(FileDetails)
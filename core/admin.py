from django.contrib import admin
from .models import Userprofile, GroupProfile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_per_page = 10    

class GroupProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_per_page = 10

admin.site.register(Userprofile, ProfileAdmin)
admin.site.register(GroupProfile, GroupProfileAdmin)


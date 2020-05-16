from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'image', 'phone_number', 'passport_number')
    list_display_links = ('user',)
    search_fields = ('user', 'phone_number', 'passport_number')


admin.site.register(Profile, ProfileAdmin)

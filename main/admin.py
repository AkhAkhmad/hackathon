from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from . import models
from .models import User, UserProfile


@admin.register(models.News)
class Admin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Image'


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

from django.contrib import admin

from reversion.admin import VersionAdmin

from apps.user.models import UserProfile

admin.site.register(UserProfile, VersionAdmin)

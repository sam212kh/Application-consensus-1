from django.contrib import admin

from reversion.admin import VersionAdmin

from apps.user.models import UserProfile

from apps.school.models import School


class SchoolInline(admin.TabularInline):
    model = School
    show_change_link = True


class UserProfileAdmin(VersionAdmin):
    inlines = [
        SchoolInline,
    ]


admin.site.register(UserProfile, UserProfileAdmin)

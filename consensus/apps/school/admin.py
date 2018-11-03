from django.contrib import admin

from reversion.admin import VersionAdmin
from apps.school.models import School

admin.site.register(School, VersionAdmin)

from django.contrib import admin

from reversion.admin import VersionAdmin
from consensus.apps.school.models import School

admin.site.register(School, VersionAdmin)

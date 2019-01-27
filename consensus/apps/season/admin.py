from django.contrib import admin

from reversion.admin import VersionAdmin
from apps.season.models import Season

admin.site.register(Season, VersionAdmin)

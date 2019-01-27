from django.contrib import admin

from reversion.admin import VersionAdmin
from apps.application.models import Application

admin.site.register(Application, VersionAdmin)

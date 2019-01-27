from django.contrib import admin

from reversion.admin import VersionAdmin
from apps.score.models import Score

admin.site.register(Score, VersionAdmin)

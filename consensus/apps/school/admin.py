from admin_view_permission.admin import AdminViewPermissionAdminSite
from django.contrib import admin

from apps.school.models import School, Application, Score, Season, Staff


class SchoolInstanceAdmin(AdminViewPermissionAdminSite):
    list_display = ('full_name', 'phone_number', 'address', 'country', 'country', 'state', 'city', 'zip_code')
    list_filter = ('full_name', 'phone_number', 'address', 'country', 'country', 'state', 'city', 'zip_code')


admin.site.register(School)
admin.site.register(Application)
admin.site.register(Score)
admin.site.register(Season)
admin.site.register(Staff)

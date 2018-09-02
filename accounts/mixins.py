from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect

class HasStaffSuperAccessMixin(AccessMixin):
    """
    CBV mixin which verifies that the current staff has super access.
    """
    permission_denied_message = 'Staff do not have permission to add staff'

    def dispatch(self, request, *args, **kwargs):
        try:
            staff = request.user.staff
            if staff.is_super_staff:
                return super(HasStaffSuperAccessMixin, self).dispatch(request, *args, **kwargs)
            else:
                return self.handle_no_permission()
        except Exception as e:
            return self.handle_no_permission()

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return HttpResponseRedirect('/')
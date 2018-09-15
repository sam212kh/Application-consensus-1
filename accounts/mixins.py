from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group

class HasStaffSuperAccessMixin(AccessMixin):
    """
    CBV mixin which verifies that the current staff has super access.
    """
    permission_denied_message = 'Staff do not have permission to add staff'

    def dispatch(self, request, *args, **kwargs):
        try:
            group = Group.objects.get(name='School')
            try:
                school = request.user.school
            except Exception as e:
                school = None
            if school or request.user.staff.is_super_staff:
                return super(HasStaffSuperAccessMixin, self).dispatch(request, *args, **kwargs)
            else:
                return self.handle_no_permission()
        except Exception as e:
            return self.handle_no_permission()

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return HttpResponseRedirect('/')

class GroupRequiredMixin(object):
    """
        group_required - list of strings, required param
    """

    group_required = None

    def dispatch(self, request, *args, **kwargs):

        user_groups = []
        for group in request.user.groups.values_list('name', flat=True):
            user_groups.append(group)
        if len(set(user_groups).intersection(self.group_required)) <= 0:
            raise PermissionDenied
        return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)
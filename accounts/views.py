from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse
from accounts.constants import *
from django.views.generic import FormView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404, render
from accounts.forms import *
from accounts.mixins import HasStaffSuperAccessMixin
from django.contrib.auth import logout


# Create your views here.
class MyLoginView(LoginView):

    template_name = "account/login.html"

    def __init__(self, **kwargs):
        super(LoginView,self).__init__(**kwargs)

    def get_success_url(self, fallback_url=None, **kwargs):
        try:
            fallback_url = reverse('dashboard')
            return fallback_url

        except Exception as e:
            pass

def Logout(request):
    logout(request)
    url = reverse("login")
    return redirect(url, args=(),kwargs={})

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


class StudentView(LoginRequiredMixin, FormView):

    template_name = 'student.html'
    form_class = StudentCreationForm

    def __init__(self, **kwargs):
        super(StudentView,self).__init__(**kwargs)

    def get_form_kwargs(self):
        kwargs = super(StudentView, self).get_form_kwargs()
        # kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(StudentView, self).get_context_data(**kwargs)
        context['school'] = self.request.user.staff.staff_school
        return context

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, 'Student create successfully.')
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('student')


class StaffView(LoginRequiredMixin, HasStaffSuperAccessMixin, FormView):

    template_name = 'staff.html'
    form_class = StaffSignupForm

    def __init__(self, **kwargs):
        super(StaffView,self).__init__(**kwargs)

    def get_form_kwargs(self):
        kwargs = super(StaffView, self).get_form_kwargs()
        # kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(StaffView, self).get_context_data(**kwargs)
        context['school'] = self.request.user.staff.staff_school
        return context

    def form_valid(self, form):
        school = self.request.user.staff.staff_school
        form.save(school)
        messages.success(
            self.request, 'Staff create successfully.')
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('staff')



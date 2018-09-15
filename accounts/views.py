from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from accounts.constants import *
from django.views.generic import FormView, TemplateView, DetailView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404, render
from accounts.forms import *
from accounts.mixins import HasStaffSuperAccessMixin, GroupRequiredMixin
from django.contrib.auth import logout
import pandas as pd
from tqdm import tqdm
from django.core.files.storage import FileSystemStorage
from django.db import transaction
from review.models import Application, Review, Offer
from accounts.models import Batch
import math
from django.db.models import Count
from datetime import  datetime, timedelta
from review.forms import ApplicationSearchForm, ApplicationStatusForm
from review.multiforms import MultiFormsView
from django.http import HttpResponseRedirect
from django.core.management import call_command


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


class CommandExecView(LoginRequiredMixin, View):
    success_url = reverse_lazy('dashboard')

    def get(self, request, *args, **kwargs):
        action = request.GET.get('action')
        call_command(action)
        messages.success(
            self.request, 'Operation has been performed.')
        return redirect(self.success_url)





class SchoolSignup(FormView):
    template_name = 'account/school_signup.html'
    form_class = SchoolSignupForm

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, 'School created successfully.')
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('login')

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
        batch_id = self.kwargs.get('pk')
        try:
            context['students'] = Batch.objects.get(id=batch_id).batch_students.all()
        except Exception as e:
            context['students'] = []
        return context

    def form_valid(self, form):
        form.save()
        # messages.success(
        #     self.request, 'Student create successfully.')
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('student')



class Applications(LoginRequiredMixin, HasStaffSuperAccessMixin, MultiFormsView):
    template_name = 'applications.html'
    form_classes = {'search': ApplicationSearchForm,
                    'status': ApplicationStatusForm,
                    }

    success_urls = {
        'search': reverse_lazy('applications'),
        'status': reverse_lazy('applications'),
    }

    def get_context_data(self, **kwargs):
        context = super(Applications, self).get_context_data(**kwargs)
        try:
            school = self.request.user.school
        except Exception as e:
            school = self.request.user.staff.staff_school

        applications = Application.objects.filter(school=school).order_by('-application_score', '-date')
        context['applications'] = applications
        return context

    def search_form_valid(self, form):
        search = form.cleaned_data.get('search')
        context = {}
        try:
            application = Application.objects.get(id=search)
            context['applications'] = [application]
        except Application.DoesNotExist:
            context['applications'] = []
        return render(self.request, self.template_name, context)

    def status_form_valid(self, form):
        id = form.cleaned_data.get('id')
        status = form.cleaned_data.get('status')
        try:
            application = Application.objects.get(id=id)
            offer = application.student.student_offer.last()
            offer.status = status
            offer.save()
            if(status == Offer.Accepted):
                application.student.student_batch = application.batch
                application.student.save()

        except Exception as e:
            print('error')
        form_name = form.cleaned_data.get('action')
        return HttpResponseRedirect(self.get_success_url(form_name))

class UploadApplications(LoginRequiredMixin, HasStaffSuperAccessMixin, FormView):
    template_name = 'upload.html'
    form_class = UploadApplicationForm

    def create_applications(self, row, school):
        with transaction.atomic():
            student = Student.objects.create(
                first_name=row['first_name'],
                last_name=row['last_name'],
                email=row['email'],
                phone_number=row['phone_number'],
                date_of_birth=row['date_of_birth'],
                gender=row['gender'],
            )
            application = Application.objects.create(
                application_text=row['application_text'],
                educational_info=row['educational_info'],
                student=student,
            )
            application.school = school
            try:
                current_batch = Batch.objects.get(batch_school=school, is_current=True)
                application.batch = current_batch
            except Exception as e:
                pass
            application.save()


    def form_valid(self, form):
        try:
            file = self.request.FILES['file']
            try:
                school = self.request.user.school
            except Exception as e:
                school = self.request.user.staff.staff_school
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            uploaded_file_url = fs.path(filename)
            states = pd.read_csv(uploaded_file_url, na_filter=False)
            for idx, row in tqdm(states.iterrows(), total=len(states)):
                print("INDEX:", row['first_name'], row['last_name'])
                self.create_applications(row, school)
            messages.success(
                self.request, 'Applications uploaded successfully.')
            return redirect(self.get_success_url())
        except Exception as e:
            print (e)

    def get_success_url(self):
        return reverse('dashboard')



class BatchView(LoginRequiredMixin, GroupRequiredMixin, FormView):
    group_required = ['School']
    template_name = 'batch.html'
    form_class = BatchForm

    def __init__(self, **kwargs):
        super(BatchView,self).__init__(**kwargs)


    def get_context_data(self, **kwargs):
        context = super(BatchView, self).get_context_data(**kwargs)
        context['batches'] = self.request.user.school.school_batches
        return context

    def form_valid(self, form):
        form.save(self.request.user.school)
        # messages.success(
        #     self.request, 'Batch created successfully.')
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('batch')

class StaffEditView(LoginRequiredMixin, UpdateView):
    form_class = StaffUpdateForm
    model = Staff
    template_name = 'edit.html'
    def get_context_data(self, **kwargs):
        context = super(StaffEditView, self).get_context_data(**kwargs)
        context['page'] = "Staff"
        return context
    def get_object(self, queryset=None):
        obj = Staff.objects.get(id=self.kwargs.get('pk'))
        return obj
    def get_success_url(self):
        return reverse('staff')

class StaffView(LoginRequiredMixin, HasStaffSuperAccessMixin, FormView):

    template_name = 'staff.html'
    form_class = StaffSignupForm

    def __init__(self, **kwargs):
        super(StaffView,self).__init__(**kwargs)

    def get_form_kwargs(self):
        kwargs = super(StaffView, self).get_form_kwargs()
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(StaffView, self).get_context_data(**kwargs)
        try:
            context['school'] = self.request.user.school
        except Exception as e:
            context['school'] = self.request.user.staff.staff_school
        return context

    def form_valid(self, form):
        try:
            school = self.request.user.school
        except Exception as e:
            school = self.request.user.staff.staff_school
        form.save(school)
        # messages.success(
        #     self.request, 'Staff created successfully.')
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('staff')




from django.urls import reverse

from django.views.generic import FormView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404, render
from review.forms import *
from review.models import Application, Review
from django.db import transaction


# Create your views here.
class ApplicationView(FormView):
    template_name = 'application.html'
    form_class = ApplicationForm

    def __init__(self, **kwargs):
        super(ApplicationView,self).__init__(**kwargs)

    def form_valid(self, form):
        try:
            with transaction.atomic():
                student = Student.objects.create(
                    first_name = form.cleaned_data.get('first_name'),
                    last_name = form.cleaned_data.get('last_name'),
                    email = form.cleaned_data.get('email'),
                    phone_number = form.cleaned_data.get('phone_number'),
                    date_of_birth = form.cleaned_data.get('date_of_birth'),
                    gender = form.cleaned_data.get('gender'),
                )
                application = Application.objects.create(
                    application_text=form.cleaned_data.get('application_text'),
                    educational_info=form.cleaned_data.get('educational_info'),
                    student=student,
                )
                application.school_id = form.cleaned_data.get('school')
                try:
                    current_batch = Batch.objects.get(batch_school__id=form.cleaned_data.get('school'), is_current=True)
                    application.batch = current_batch
                except Exception as e:
                    pass
                application.save()
                messages.success(
                    self.request, 'Application submitted successfully.')
            return redirect(self.get_success_url())
        except Exception as e:
            super(ApplicationView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('application-submit')


class ReviewView(TemplateView):
    template_name = 'review-applications.html'

    def get_context_data(self, **kwargs):
        context = super(ReviewView, self).get_context_data(**kwargs)
        reviews = self.request.user.staff.staff_review.filter(is_rated = False)
        applications = []
        for review in reviews:
            if review.application.status == Application.NotScored:
                applications.append({"id": review.id,"application": review.application})
        context['objs'] = applications
        return context


class ReviewDetailView(FormView):
    template_name = 'rate-applications.html'
    form_class = RateForm

    def get_context_data(self, **kwargs):
        context = super(ReviewDetailView, self).get_context_data(**kwargs)
        review_id = self.kwargs.get('pk')
        review = self.request.user.staff.staff_review.get(id=review_id)
        context['application'] = review.application
        return context

    def form_valid(self, form):
        review_id = self.kwargs.get('pk')
        rating = form.cleaned_data.get('rating')
        comment = form.cleaned_data.get('comment')
        try:
            with transaction.atomic():
                review= Review.objects.get(id=review_id)
                review.rating = int(rating)
                review.comment = comment
                review.is_rated = True
                review.save()
                return redirect(self.get_success_url())
        except Exception as e:
            super(ReviewDetailView, self).form_invalid(form)

    def get_success_url(self):
        return reverse('application-review')
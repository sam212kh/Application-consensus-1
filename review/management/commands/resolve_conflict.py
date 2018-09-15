from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from django.utils import timezone

from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from review.models import Application, Review
from accounts.models import School, Staff
import math
from django.db.models import Count



class Command(BaseCommand):
    help = 'resolve conflict and reassign if conflict not resolved.'

    def handle(self, *args, **options):
        schools = School.objects.filter(school_batches__is_current=True)
        for school in schools:
            reviews_required = school.application_reviews_required
            minumum_acceptance = math.floor(reviews_required * 0.75)
            applications = school.school_applications.all()
            for application in applications:
                if application.status != Application.Scored:
                    all_reviews = Review.objects.filter(application=application)
                    rated_reviews = all_reviews.filter(is_rated=True)
                    if len(rated_reviews) > 0:
                        top_rating_obj = \
                        rated_reviews.filter(is_rated=True).values('rating').annotate(total=Count('rating')).order_by(
                            '-total')[0]
                        if top_rating_obj['total'] >= minumum_acceptance:
                            application.application_score = top_rating_obj['rating']
                            application.status = Application.Scored
                            application.save()
                        elif len(all_reviews) == len(rated_reviews):
                            staffs = Staff.objects.filter(staff_school=school)
                            re_assigned = False
                            staffs_assigned_application = all_reviews.values_list('staff', flat=True)
                            for staff in staffs:
                                if staff.id not in staffs_assigned_application:
                                    Review.objects.create(application=application, staff=staff)
                                    re_assigned = True
                                    break
                            if not re_assigned:
                                print("conflict cannot be resolved, resolve it manually.");

                        else:
                            pass



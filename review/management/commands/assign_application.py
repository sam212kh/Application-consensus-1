from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from django.utils import timezone

from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from review.models import Application, Review
from accounts.models import School
class Command(BaseCommand):
    help = 'assign applications to staff for review'

    def handle(self, *args, **options):
        schools = School.objects.filter(school_batches__is_current=True)
        for school in schools:
            reviews_required = school.application_reviews_required
            # reviews_required = 2
            applications = school.school_applications.all()
            staffs = school.school_staffs.all()
            if reviews_required > len(staffs):
                print("cannot assign applications for review, school is under staffed. ")
                continue
            start = 0 % len(staffs)
            for application in applications:
                for staff in staffs[start: start + reviews_required]:
                    Review.objects.create(application=application, staff=staff)
                start = (start + reviews_required)
                if start >= len(staffs):
                    start = 0
                if start + reviews_required > len(staffs):
                    start = start - (start + reviews_required - len(staffs))
        print('applications assigned.')
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from django.utils import timezone

from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from review.models import Application, Review, Offer
from accounts.models import School, Batch
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'dispatch offer to students'

    def handle(self, *args, **options):
        schools = School.objects.filter(school_batches__is_current=True)
        for school in schools:
            try:
                current_batch = Batch.objects.get(batch_school=school, is_current=True)
                applications = Application.objects.filter(school=school, status=Application.Scored).order_by('application_score', 'date')
                offer_count = 0
                for application in applications:
                    offer = application.student.student_offer.last()
                    if offer:
                        if offer.status == Offer.Pending or offer.status == Offer.Accepted:
                            offer_count += 1
                    else:
                        if offer_count < current_batch.max_batch_size:
                            Offer.objects.create(student=application.student, school=application.school,
                                             expire_at=datetime.now() + timedelta(days=10))
                        else:
                            break

            except Batch.DoesNotExist:
                print("no batch active")

            except Exception as e:
                print("something went wrong")
        print('offers dispatched.')
from __future__ import unicode_literals
import pytz
from django.db import models
from accounts.models import Student, School, Staff, Batch


class Application(models.Model):
    NotScored = 'NotScored'
    Scored = 'Scored'
    STATUS_CHOICES = (
        (NotScored, 'Application not scored'),
        (Scored, 'Application scored'),
    )
    application_text = models.CharField(max_length=1000)
    educational_info = models.CharField(max_length=1000, null=True, blank=True)
    student = models.ForeignKey(Student, related_name='student_application', on_delete=models.CASCADE)
    school = models.ForeignKey(School, related_name='school_applications', on_delete=models.CASCADE, null=True, blank=True)
    batch = models.ForeignKey(Batch, related_name='batch_applications', on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=NotScored)
    application_score = models.IntegerField(default=0)
    date = models.DateField(auto_now=True)

class Review(models.Model):
    application = models.ForeignKey(Application, related_name='application_review', on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, related_name='staff_review', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.CharField(max_length=255, null=True, blank=True)
    is_rated = models.BooleanField(default=False)

class Offer(models.Model):
    Pending = 'Pending'
    Accepted = 'Accepted'
    Rejected = 'Rejected'
    Expired = 'Expired'
    STATUS_CHOICES = (
        (Pending, 'Offer pending'),
        (Accepted, 'Offer accepted'),
        (Rejected, 'Offer rejected'),
        (Expired, 'Offer expired'),
    )
    student = models.ForeignKey(Student, related_name='student_offer', on_delete=models.CASCADE)
    school = models.ForeignKey(School, related_name='school_offers', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=Pending)
    start_at = models.DateField(auto_now=True)
    expire_at = models.DateField()

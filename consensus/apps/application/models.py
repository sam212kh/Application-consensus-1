import reversion

from django.db import models
from apps.school.models import School

@reversion.register()
class Application(models.Model):

    GENDER_UNKNOWN = 'u'
    GENDER_MALE = 'm'
    GENDER_FEMALE = 'f'
    GENDER_CHOICES = (
        (GENDER_UNKNOWN, 'Unknown'),
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    )

    school_id = models.ForeignKey(
        School,
        related_name='application',
        default='0',
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField('Date of birth', blank=True, null=True)
    gender = models.CharField('Gender', max_length=1, choices=GENDER_CHOICES, default=GENDER_UNKNOWN)
    phone_number  = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    info = models.CharField(max_length=255, null=True, blank=True)
    educational_info = models.CharField(max_length=255, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.full_name

import reversion

from django.db import models
from apps.school.models import School

@reversion.register()
class Staff(models.Model):

    school_id = models.ForeignKey(
        School,
        related_name='staff',
        default='0',
        on_delete=models.CASCADE
    )

    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255, null=True, blank=True)
    phone_number  = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    user_name = models.CharField(max_length=255, unique=True)


    def __str__(self):
        return self.first_name

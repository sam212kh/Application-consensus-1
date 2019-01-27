import reversion

from django.db import models
from apps.school.models import School
from apps.staff.models import Staff
from apps.application.models import Application

@reversion.register()
class Score(models.Model):
    school_id = models.ForeignKey(
        School,
        related_name='score_school',
        default='0',
        on_delete=models.CASCADE
    )

    application_id = models.ForeignKey(
        Application,
        related_name='score_application',
        default='0',
        on_delete=models.CASCADE
    )

    staff_id = models.ForeignKey(
        Staff,
        related_name='score_staff',
        default='0',
        on_delete=models.CASCADE
    )

    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255, null=True, blank=True)
    score_date = models.DateTimeField(auto_now_add=True,null=True)
    score = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.full_name

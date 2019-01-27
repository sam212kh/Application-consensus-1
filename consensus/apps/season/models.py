import reversion

from django.db import models
from apps.school.models import School

@reversion.register()
class Season(models.Model):
    full_name = models.CharField(max_length=255)
    school_id = models.ForeignKey(
        School,
        related_name='school',
        default='0',
        on_delete=models.CASCADE
    )
    kind = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True,null=True)
    end_date = models.DateTimeField(auto_now_add=True,null=True)
    info = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.full_name

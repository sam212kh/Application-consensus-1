import reversion

from django.db import models


@reversion.register()
class School(models.Model):
    full_name = models.CharField(max_length=255)
    user_id   = models.ForeignKey(
        'auth.User',
        default='0',
        on_delete=models.CASCADE
    )
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    application_reviews_required = models.IntegerField(help_text="Reviews required for each application received",
                                                       default=3)

    def __str__(self):
        return self.full_name

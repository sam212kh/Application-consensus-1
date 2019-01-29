import reversion

from django.db import models

from apps.user.models import UserProfile
from django.db.models import CASCADE


@reversion.register()
class School(models.Model):
    full_name = models.CharField(max_length=255)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, editable=False)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    grade = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    application_reviews_required = models.IntegerField(help_text="Reviews required for each application received",
                                                       default=3)

    def __str__(self):
        return self.full_name


@reversion.register()
class Staff(models.Model):
    school = models.ForeignKey(
        School,
        related_name='school_staff',
        default='0',
        on_delete=models.CASCADE
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    user_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.first_name


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

    school = models.ForeignKey(
        School,
        related_name='school_application',
        default='0',
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField('Date of birth', blank=True, null=True)
    gender = models.CharField('Gender', max_length=1, choices=GENDER_CHOICES, default=GENDER_UNKNOWN)
    phone_number = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    info = models.CharField(max_length=255, null=True, blank=True)
    educational_info = models.CharField(max_length=255, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.full_name


@reversion.register()
class Score(models.Model):
    application_id = models.ForeignKey(
        Application,
        related_name='application_score',
        default='0',
        on_delete=models.CASCADE
    )

    staff = models.ForeignKey(
        Staff,
        related_name='staff_score',
        default='0',
        on_delete=models.CASCADE
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    score_date = models.DateTimeField(auto_now_add=True, null=True)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.full_name


@reversion.register()
class Season(models.Model):
    full_name = models.CharField(max_length=255)
    school = models.ForeignKey(
        School,
        related_name='school_season',
        default='0',
        on_delete=models.CASCADE
    )
    kind = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True, null=True)
    end_date = models.DateTimeField(auto_now_add=True, null=True)
    info = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.full_name

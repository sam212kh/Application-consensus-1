import reversion

from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


@reversion.register()
class School(models.Model):
    full_name = models.CharField(max_length=255)
    participations = models.ManyToManyField(User, through='Participation', through_fields=('school', 'participant'))
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
    user = models.OneToOneField(User, primary_key=False, related_name='user',
                                on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.first_name


@reversion.register()
class Participation(models.Model):
    PARTICIPATION_OWNER = 'o'
    PARTICIPATION_STAFF = 's'
    PARTICIPATION_CHOICES = (
        (PARTICIPATION_OWNER, 'Owner'),
        (PARTICIPATION_STAFF, 'Staff'),
    )
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    participation_date = models.DateField()
    participation_type = models.CharField('Participation', max_length=1, choices=PARTICIPATION_CHOICES)

    def __init__(self, school, participant, participation_date, participation_type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.school = school
        self.participant = participant
        self.participation_date = participation_date
        self.participation_type = participation_type

    def __str__(self):
        return self.participation_type


@reversion.register()
class Season(models.Model):
    full_name = models.CharField(max_length=255)
    school = models.ForeignKey(
        School,
        related_name='season',
        on_delete=models.CASCADE
    )
    kind = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True, null=True)
    end_date = models.DateTimeField(auto_now_add=True, null=True)
    info = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.full_name


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

    season = models.ForeignKey(
        Season,
        related_name='application',
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
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.first_name


@reversion.register()
class Score(models.Model):
    application = models.ForeignKey(
        Application,
        related_name='score',
        on_delete=models.CASCADE
    )

    staff = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    score_date = models.DateTimeField(auto_now_add=True, null=True)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.score

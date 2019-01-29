import os

from django.contrib.auth import get_user_model
from django.db import models

from consensus.helpers.utils import get_random_upload_path

User = get_user_model()


def avatar_file_path_func(instance, filename):
    return get_random_upload_path(os.path.join('uploads', 'profile_avatar'), filename)


class UserProfile(models.Model):
    GENDER_UNKNOWN = 'u'
    GENDER_MALE = 'm'
    GENDER_FEMALE = 'f'
    GENDER_CHOICES = (
        (GENDER_UNKNOWN, 'Unknown'),
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    )

    user = models.OneToOneField(User, primary_key=True, related_name='profile',
                                on_delete=models.CASCADE)
    birth_date = models.DateField('Date of birth', blank=True, null=True)
    gender = models.CharField('Gender', max_length=1, choices=GENDER_CHOICES, default=GENDER_UNKNOWN)
    avatar = models.ImageField('Avatar', blank=True, null=True, upload_to=avatar_file_path_func)

    def __str__(self):
        return '{}'.format(self.user)


# Create your models here.

from __future__ import unicode_literals

import pytz
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,
    PermissionsMixin, Group)
from django.contrib.auth.models import Permission
from accounts.constants import *
import datetime

class UserManager(BaseUserManager):

    def create_school(self, username, **fields):
        if not fields['email']:
            raise ValueError('Users must have an email address')

        school = School(
            username=username,
            email=self.normalize_email(fields['email']),
            name=self.normalize_email(fields['name']),
            address=self.normalize_email(fields['address']),
            phone_number=self.normalize_email(fields['phone']),
            country=self.normalize_email(fields['country']),
            state=self.normalize_email(fields['state']),
            city=self.normalize_email(fields['city']),
            zip_code=self.normalize_email(fields['zip_code']),
        )
        if 'password' in fields:
            school.set_password(fields['password'])
        else:
            school.set_unusable_password()

        group = Group.objects.get(name='School')
        school.groups.add(group)

        school.save(using=self._db)
        return school

    def create_super_staff(self, username, school, **fields):
        if not fields['email']:
            raise ValueError('Users must have an email address')

        staff = Staff(
            username=username,
            email=self.normalize_email(fields['email']),
            first_name=self.normalize_email(fields['first_name']),
            last_name=self.normalize_email(fields['last_name']),
            phone_number=self.normalize_email(fields['phone']),
            is_super_staff=True,
            staff_school=school,
        )
        if 'password' in fields:
            staff.set_password(fields['password'])
        else:
            staff.set_unusable_password()

        group = Group.objects.get(name='Staff')
        staff.groups.add(group)

        permission = Permission.objects.get(codename='can_create_staff')
        staff.user_permissions.add(permission)

        staff.save(using=self._db)
        return staff

    def create_staff(self, username, school, **fields):
        if not fields['email']:
            raise ValueError('Users must have an email address')

        staff = Staff(
            username=username,
            email=self.normalize_email(fields['email']),
            first_name=self.normalize_email(fields['first_name']),
            last_name=self.normalize_email(fields['last_name']),
            phone_number=self.normalize_email(fields['phone']),
            is_super_staff=False,
            staff_school=school,
        )
        if 'password' in fields:
            staff.set_password(fields['password'])
        else:
            staff.set_unusable_password()

        group = Group.objects.get(name='Staff')
        staff.groups.add(group)

        staff.save(using=self._db)
        return staff

    def create_superuser(self, username, **fields):
        """
        Creates and saves a superuser with the given email, and password.
        """
        user = self.model(
            username=username,
            email=self.normalize_email(fields['email']),
        )
        if 'password' in fields:
            user.set_password(fields['password'])
        else:
            user.set_unusable_password()
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        user.save(using=self._db)

        try:
            Group.objects.get(name='Admin')
        except ObjectDoesNotExist:
            Group.objects.create(name='Admin')
            Group.objects.create(name='School')
            Group.objects.create(name='Staff')
            Group.objects.create(name='Student')

        group = Group.objects.get(name='Admin')
        user.groups.add(group)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_username(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_user_group(self):
        try:
            return GROUPS[self.groups.all()[0].name]
        except:
            return GROUPS['Client']

class School(User, PermissionsMixin):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    application_reviews_required = models.IntegerField(help_text="Reviews required for each application received", default=3)


class Staff(User, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    is_super_staff = models.BooleanField(default=False)
    staff_school = models.ForeignKey(School, related_name='school_staffs', on_delete=models.CASCADE)

    class Meta:
        permissions = (("can_create_staff", "Create new staff"),)

    def has_perm(self, perm, obj=None):
        return self.is_super_staff


class Department(models.Model):
    name = models.CharField(max_length=255)
    department_school = models.ForeignKey(School, related_name='school_departments', on_delete=models.CASCADE)


class Batch(models.Model):
    YEAR_CHOICES = []
    for r in range(datetime.datetime.now().year, (datetime.datetime.now().year + 10)):
        YEAR_CHOICES.append((r, r))

    name = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    batch_school = models.ForeignKey(School, related_name='school_batches', on_delete=models.CASCADE)
    application_acceptance_start_at = models.DateField()
    application_acceptance_end_at = models.DateField()
    max_batch_size = models.IntegerField(help_text="Maximum students to enroll each year in a batch", null=True, blank=True)
    is_current = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.is_current:
            qs = type(self).objects.filter(is_current=True)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            qs.update(is_current=False)
        super(Batch, self).save(*args, **kwargs)


class Student(models.Model):
    Male = 'Male'
    Female = 'Female'
    STATUS_CHOICES = (
        (Male, 'Male'),
        (Female, 'Female'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255)
    student_batch = models.ForeignKey(Batch, related_name='batch_students', on_delete=models.CASCADE, null=True, blank=True)

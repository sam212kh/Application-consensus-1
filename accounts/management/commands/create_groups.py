from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from django.utils import timezone

from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'create groups'

    def handle(self, *args, **options):

        try:
            Group.objects.get(name='Admin')
        except ObjectDoesNotExist:
            Group.objects.create(name='Admin')
            Group.objects.create(name='School')
            Group.objects.create(name='Staff')
            Group.objects.create(name='Student')
        print ('command executed.')
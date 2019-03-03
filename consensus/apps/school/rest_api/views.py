from apps.school.models import School, Application, Score, Season, Staff, Participation
from apps.school.rest_api.serializers import SchoolSerializer, ApplicationSerializer, ScoreSerializer, SeasonSerializer, \
    StaffSerializer
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from djoser.serializers import UserSerializer
from requests import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied

from apps.school.models import User


class SchoolBasedViewMixin(object):
    _base_school = None
    school_base_rel = 'school'

    @property
    def base_school_id(self):
        return self.kwargs.get('_school_pk')

    @property
    def base_school(self):
        if not self._base_school:
            self._base_school = get_object_or_404(School.objects.all(), pk=self.base_school_id)
        return self._base_school

    def get_queryset(self):
        qs = super(SchoolBasedViewMixin, self).get_queryset()
        if self.school_base_rel:
            qs = qs.filter(**{self.school_base_rel: self.base_school_id})
        return qs


class SeasonBasedViewMixin(object):
    _base_season = None
    season_base_rel = 'season'

    @property
    def base_season_id(self):
        return self.kwargs.get('_season_pk')

    @property
    def base_season(self):
        if not self._base_season:
            self._base_season = get_object_or_404(Season.objects.all(), pk=self.base_season_id)
        return self._base_season

    def get_queryset(self):
        qs = super(SeasonBasedViewMixin, self).get_queryset()
        if self.season_base_rel:
            qs = qs.filter(**{self.season_base_rel: self.base_season_id})
        return qs






class ApplicationBasedViewMixin(object):
    _base_application = None
    application_base_rel = 'application'

    @property
    def base_application_id(self):
        return self.kwargs.get('_application_pk')

    @property
    def base_application(self):
        if not self._base_application:
            self._base_application = get_object_or_404(Application.objects.all(), pk=self.base_application_id)
        return self._base_application

    def get_queryset(self):
        qs = super(ApplicationBasedViewMixin, self).get_queryset()
        if self.application_base_rel:
            qs = qs.filter(**{self.application_base_rel: self.base_application_id})
        return qs


class SchoolView(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    ordering = 'id'
    ordering_fields = '__all__'

    def get_queryset(self):
        # All schools that the current user has participation with them
        return self.queryset.filter(participation__participant=self.request.user.id)

    def perform_update(self, serializer):
        # If the current user is the owner of the given school
        participation = Participation.objects.filter(
            school=serializer.instance,
            participant=self.request.user,
            participation_type=Participation.PARTICIPATION_OWNER
        ).first()
        if participation:
            serializer.save()
        else:
            raise PermissionDenied

    def perform_destroy(self, instance):
        # If the current user is the owner of the given school
        participation = Participation.objects.filter(
            school=instance,
            participant=self.request.user,
            participation_type=Participation.PARTICIPATION_OWNER
        ).first()
        if participation:
            instance.delete()
        else:
            raise PermissionDenied


class StaffView(SchoolBasedViewMixin, viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    ordering = 'first_name'
    ordering_fields = '__all__'

    def get_queryset(self):
        # If the current user is the owner of the given school
        participation = Participation.objects.filter(
            school=self.base_school_id,
            participant=self.request.user,
            participation_type=Participation.PARTICIPATION_OWNER
        ).first()
        if not participation:
            raise PermissionDenied

        # All staffs that have participation with the given school
        return self.queryset.filter(
            user__participation__school=self.base_school_id,
            user__participation__participation_type=Participation.PARTICIPATION_STAFF
        )

    @action(detail=False, methods=['POST'])
    def invite(self, request, *args, **kwargs):
        # If the current user is the owner of the given school
        participation = Participation.objects.filter(
            school=self.base_school_id,
            participant=self.request.user,
            participation_type=Participation.PARTICIPATION_OWNER
        ).first()
        if participation:
            filter_by_email_or_user_name = \
                Staff.objects.filter(email=kwargs.get('email')) | \
                Staff.objects.filter(user_name=kwargs.get('user_name'))
            staff = filter_by_email_or_user_name.first()
            if staff:
                send_mail("It works!", "Invitation email",
                          "Anymail Sender <from@example.com>", ["to@example.com"])
            else:
                send_mail("It works!", "Sign up email",
                          "Anymail Sender <from@example.com>", ["to@example.com"])
        else:
            raise PermissionDenied

    def perform_create(self, serializer):
        # If the current user is the owner of the given school
        participation = Participation.objects.filter(
            school=self.base_school_id,
            participant=self.request.user,
            participation_type=Participation.PARTICIPATION_OWNER
        ).first()
        if participation:
            serializer.save()
        else:
            raise PermissionDenied

    def perform_update(self, serializer):
        # If the current user is the owner of the given school
        participation = Participation.objects.filter(
            school=self.base_school_id,
            participant=self.request.user,
            participation_type=Participation.PARTICIPATION_OWNER
        ).first()
        if participation:
            serializer.save()
        else:
            raise PermissionDenied

    def perform_destroy(self, instance):
        # If the current user is the owner of the given school
        participation = Participation.objects.filter(
            school=self.base_school_id,
            participant=self.request.user,
            participation_type=Participation.PARTICIPATION_OWNER
        ).first()
        if participation:
            instance.delete()
        else:
            raise PermissionDenied


class SeasonView(SchoolBasedViewMixin, viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    ordering = 'start_date'
    ordering_fields = '__all__'

    def get_queryset(self):
        # If the current user has participation with the given school
        participation = Participation.objects.filter(
            school=self.base_school_id,
            participant=self.request.user
        ).first()
        if not participation:
            raise PermissionDenied

        # All school's seasons
        return self.queryset.filter(school=self.base_school_id)

    def perform_create(self, serializer):
        # If the current user is the owner of the given school
        participation = Participation.objects.filter(
            school=self.base_school_id,
            participant=self.request.user,
            participation_type=Participation.PARTICIPATION_OWNER
        ).first()
        if participation:
            serializer.save()
        else:
            raise PermissionDenied

    def perform_update(self, serializer):
        # If the current user is the owner of the given school
        participation = Participation.objects.filter(
            school=self.base_school_id,
            participant=self.request.user,
            participation_type=Participation.PARTICIPATION_OWNER
        ).first()
        if participation:
            serializer.save()
        else:
            raise PermissionDenied

    def perform_destroy(self, instance):
        # If the current user is the owner of the given school
        participation = Participation.objects.filter(
            school=self.base_school_id,
            participant=self.request.user,
            participation_type=Participation.PARTICIPATION_OWNER
        ).first()
        if participation:
            instance.delete()
        else:
            raise PermissionDenied


class ApplicationView(SeasonBasedViewMixin, viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    ordering = 'email'
    ordering_fields = '__all__'

    def get_queryset(self):
        # If the current user has participation with the given school
        participation = Participation.objects.filter(
            school=self.base_season.school,
            participant=self.request.user
        ).first()
        if not participation:
            raise PermissionDenied

        # All school's applications for the given season
        return self.queryset.filter(season__school=self.base_season.school)

    def perform_create(self, serializer):
        # If the current user has participation with the given school
        participation = Participation.objects.filter(
            school=self.base_season.school,
            participant=self.request.user
        ).first()
        if participation:
            serializer.save()
        else:
            raise PermissionDenied

    def perform_update(self, serializer):
        # If the current user has participation with the given school
        participation = Participation.objects.filter(
            school=self.base_season.school,
            participant=self.request.user
        ).first()
        if participation:
            serializer.save()
        else:
            raise PermissionDenied

    def perform_destroy(self, instance):
        # If the current user has participation with the given school
        participation = Participation.objects.filter(
            school=self.base_season.school,
            participant=self.request.user
        ).first()
        if participation:
            instance.delete()
        else:
            raise PermissionDenied


class ScoreView(ApplicationBasedViewMixin, viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    ordering = 'score_date'
    ordering_fields = '__all__'

    def perform_create(self, serializer):
        return serializer.save(staff=self.request.user)

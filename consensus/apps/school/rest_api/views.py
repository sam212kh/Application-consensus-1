from apps.school.models import School, Application, Score, Season, Staff, Participation
from apps.school.rest_api.serializers import SchoolSerializer, ApplicationSerializer, ScoreSerializer, SeasonSerializer, \
    StaffSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from rest_framework.views import APIView

from rest_framework.response import Response


class CreateUser(viewsets.ModelViewSet):

    def signup(request,version):
        if request.method == 'POST':
            user = User.objects.create(
                    username=request.POST['username'],
                    email=request.POST['email'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    #country=request.POST.get('country'),
                    #city=request.POST.get('city'),
                    #phone_number=request.POST.get('phone_number'),

                )
            user.set_password(str(request.POST.get('password')))
            user.save()
            return Response({"status":"success","response":"User Successfully Created"}, status=status.HTTP_201_CREATED)

    def create(self, validated_data):
        if validated_data.get('password'):
            validated_data['password'] = make_password(
                validated_data['password']
            )

        user = get_user_model().objects.create(**validated_data)


        return user


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

    # def list(self, request, *args, **kwargs):
    #     # return Response(data.data)
    #     queryset = School.objects.filter(owner=self.request.user.id).only('id', 'full_name')
    #     se = Season.objects.prefetch_related('school')
    #     serializer = self.get_serializer(queryset, many=True)
    #     ser = serialize('json', se)
    #
    #     custom_data = {
    #         'list_of_items': serializer.data,
    #         'seasons ': ser
    #     }
    #
    #     return Response(custom_data)


class StaffView(SchoolBasedViewMixin, viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    ordering = 'first_name'
    ordering_fields = '__all__'


class SeasonView(SchoolBasedViewMixin, viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    ordering = 'start_date'
    ordering_fields = '__all__'


class ApplicationView(SeasonBasedViewMixin, viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    ordering = 'email'
    ordering_fields = '__all__'


class ScoreView(ApplicationBasedViewMixin, viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    ordering = 'score_date'
    ordering_fields = '__all__'

    def perform_create(self, serializer):
        return serializer.save(staff=self.request.user)

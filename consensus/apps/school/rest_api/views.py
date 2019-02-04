from apps.school.models import School, Application, Score, Season, Staff
from apps.school.rest_api.serializers import SchoolSerializer, ApplicationSerializer, ScoreSerializer, SeasonSerializer, \
    StaffSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


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
            self._base_season = get_object_or_404(School.objects.all(), pk=self.base_season_id)
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
            self._base_application = get_object_or_404(School.objects.all(), pk=self.base_application_id)
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

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user).only('id', 'full_name')

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


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

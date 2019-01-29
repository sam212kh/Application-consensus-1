from apps.school.models import School, Application, Score, Season, Staff
from apps.school.rest_api.serializers import SchoolSerializer, ApplicationSerializer, ScoreSerializer, SeasonSerializer, StaffSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class SchoolView(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    ordering = 'id'
    ordering_fields = '__all__'

    # def list(self, request, *args, **kwargs):
    #     # return Response(data.data)
    #     queryset = School.objects.filter(owner=self.request.user.id).only('id', 'full_name').all()
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
        return self.queryset.filter(owner=self.request.user).only('id', 'full_name').all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ApplicationView(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    ordering = 'id'
    ordering_fields = '__all__'


class ScoreView(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    ordering = 'id'
    ordering_fields = '__all__'


class SeasonView(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    ordering = 'id'
    ordering_fields = '__all__'
    

class StaffView(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    ordering = 'id'
    ordering_fields = '__all__'

    def get_object(self):
        return Staff.objects.filter(school_id=self.kwargs.get('id')).all()

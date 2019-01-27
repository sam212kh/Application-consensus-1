from apps.school.models import School
from apps.season.models import Season
from apps.school.rest_api.serializers import SchoolSerializer
from apps.season.rest_api.serializers import SeasonSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum
from django.db.models import Count
from rest_framework import serializers
from apps.school import models
from django.core.serializers import serialize


class SchoolsSerializer(serializers.ModelSerializer):
        class Meta:
            fields = (
                'id',
                'full_name',
                )
            model = School


class SchoolView(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    ordering = 'id'
    ordering_fields = '__all__'

    def list(self, request, *args, **kwargs):

        #return Response(data.data)
        queryset = School.objects.filter(user_id=self.request.user.id).only('id', 'full_name').all()
        se = Season.objects.prefetch_related('school_id')
        serializer = self.get_serializer(queryset, many=True)
        ser = serialize('json', se)

        custom_data = {
        'list_of_items': serializer.data,
        'seasons ' : ser
        }

        return Response(custom_data)

    def get_queryset(self):
        return School.objects.filter(user_id=self.request.user.id).only('id', 'full_name').all()


    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

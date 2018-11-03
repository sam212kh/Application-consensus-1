from consensus.apps.school.models import School
from consensus.apps.school.rest_api.serializers import SchoolSerializer
from rest_framework import viewsets


class SchoolView(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    ordering = 'id'
    ordering_fields = '__all__'

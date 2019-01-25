from apps.school.models import School
from apps.school.rest_api.serializers import SchoolSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class SchoolView(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    ordering = 'id'
    ordering_fields = '__all__'

    def get_queryset(self):
        return School.objects.filter(user_id=self.request.user.id).only('id', 'full_name').all()

    def preform_create(self, serializer):
        return serializer.save(user_id=self.request.user.id)

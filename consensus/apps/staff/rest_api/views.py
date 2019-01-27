from apps.staff.models import Staff
from apps.staff.rest_api.serializers import StaffSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



class StaffView(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    ordering = 'id'
    ordering_fields = '__all__'


    def get_object(self):
        return Staff.objects.filter(school_id=self.kwargs.get('id')).get()

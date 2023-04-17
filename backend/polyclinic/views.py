from .serializers import *
from .models import *
from rest_framework import permissions
from rest_framework import viewsets

# Create your views here.


class DoctorsViewSet(viewsets.ModelViewSet):
    queryset = Doctors.objects.all()
    serializer_class = Doctors
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ('specialization_id',)


class DoctorsSpecializationsViewSet(viewsets.ModelViewSet):
    queryset = DoctorsSpecializations.objects.all()
    serializer_class = DoctorsSpecializations
    permission_classes = [permissions.IsAuthenticated]

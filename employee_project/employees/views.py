from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from rest_framework.filters import OrderingFilter
from django.shortcuts import render

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_fields = ['department', 'date_of_joining']
    search_fields = ['name', 'email']
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name', 'date_of_joining']
    ordering = ['name']  # default sort

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

def charts_view(request):
    return render(request, 'charts.html')
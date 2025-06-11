from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from rest_framework.filters import OrderingFilter
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views import View
from rest_framework.authtoken.views import ObtainAuthToken

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

def home_view(request):
    return render(request, 'home.html')

@method_decorator(csrf_exempt, name='dispatch')
class CustomTokenAuthView(ObtainAuthToken):
    def get(self, request, *args, **kwargs):
        return JsonResponse({
            "info": "Send POST with username & password to get token.",
            "example": {"username": "admin", "password": "admin123"}
        })
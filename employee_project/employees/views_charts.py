from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from django.db.models import Count

@api_view(['GET'])
def employees_per_department(request):
    data = Employee.objects.values('department__name').annotate(count=Count('id'))
    chart_data = {
        "labels": [d['department__name'] or "Unassigned" for d in data],
        "values": [d['count'] for d in data]
    }
    return Response(chart_data)

from .models import Attendance
from django.db.models.functions import TruncMonth
from django.db.models import Count

@api_view(['GET'])
def monthly_attendance_overview(request):
    data = (
        Attendance.objects
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    chart_data = {
        "labels": [d['month'].strftime("%B %Y") for d in data],
        "values": [d['count'] for d in data]
    }
    return Response(chart_data)

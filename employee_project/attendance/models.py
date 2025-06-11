from django.db import models
from employees.models import Employee

class Attendance(models.Model):
    employee = models.ForeignKey(
        'employees.Employee',  # or Employee if directly imported
        on_delete=models.CASCADE,
        related_name='attendance_entries'  # unique
    )
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ])

class Performance(models.Model):
    employee = models.ForeignKey(
        'employees.Employee',  # or Employee if directly imported
        on_delete=models.CASCADE,
        related_name='performance_reviews'  # unique
    )
    rating = models.IntegerField()
    review_date = models.DateField()

from django.core.management.base import BaseCommand
from faker import Faker
import random
from employees.models import Employee, Department
from attendance.models import Attendance
from employees.models import Performance
from datetime import timedelta, date

fake = Faker()

class Command(BaseCommand):
    help = 'Seed database with employees, departments, attendance, and performance'

    def handle(self, *args, **kwargs):
        departments = ['HR', 'Engineering', 'Sales', 'Marketing', 'Finance']
        for dept_name in departments:
            Department.objects.get_or_create(name=dept_name)

        for _ in range(50):
            department = Department.objects.order_by('?').first()
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number()[:15],
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-5y', end_date='today'),
                department=department
            )

            # Add attendance records
            for _ in range(10):
                Attendance.objects.create(
                    employee=emp,
                    date=fake.date_between(start_date='-30d', end_date='today'),
                    status=random.choice(['Present', 'Absent', 'Late'])
                )

            # Add performance records
            for _ in range(3):
                Performance.objects.create(
                    employee=emp,
                    rating=random.randint(1, 5),
                    review_date=fake.date_between(start_date='-1y', end_date='today')
                )

        self.stdout.write(self.style.SUCCESS('✅ Seeded 50 employees with attendance and performance data.'))

"""
URL configuration for employee_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from employees.views import EmployeeViewSet, DepartmentViewSet
from attendance.views import AttendanceViewSet, PerformanceViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from employees.views import charts_view
from employees.views import home_view
from employees.views import CustomTokenAuthView





router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'performance', PerformanceViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Employee API",
      default_version='v1',
      description="API documentation for Employee Management System",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('employees.urls')),  # or whatever your app's urls file is
    path('api-token-auth/', obtain_auth_token),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Token auth endpoint
    path('dashboard/', charts_view, name='charts-dashboard'),
    path('', home_view, name='home'),
    path('api-token-auth/', CustomTokenAuthView.as_view(), name='custom-token-auth'),    # For POST
]
urlpatterns += [
    path('api-token-auth/', obtain_auth_token),
]



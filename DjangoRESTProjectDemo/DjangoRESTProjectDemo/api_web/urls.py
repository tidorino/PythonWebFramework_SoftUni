from django.urls import path

from DjangoRESTProjectDemo.api_web.views import EmployeesListApiView

urlpatterns = (
    path('employees/', EmployeesListApiView.as_view(), name='api list employees'),
)

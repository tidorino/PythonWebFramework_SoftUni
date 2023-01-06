from django.shortcuts import render
from rest_framework import generics as rest_views, serializers
from rest_framework import views as rest_base_views
from rest_framework.response import Response

from DjangoRESTProjectDemo.api_web.models import Employee, Department
from DjangoRESTProjectDemo.api_web.serializers import DepartmentSerializer, EmployeeSerializer,\
    DemoSerializer


# JSON serialization, i.e. parse models into JSON
class DepartmentsListApiView(rest_views.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeesListApiView(rest_views.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        department_id = self.request.query_params.get('department_id')
        queryset = self.queryset

        if department_id:
            queryset = queryset.filter(department_id=department_id)

        return queryset.all()



class DemoApiView(rest_base_views.APIView):
        def get(self, request):
            employees = Employee.objects.all()
            departments = Department.objects.all()

            body = {
                'employees': employees,
                'employees_count': employees.count(),
                'departments': departments,
                'first_department': departments.first(),
            }

            serializer = DemoSerializer(body)

            return Response(serializer.data)

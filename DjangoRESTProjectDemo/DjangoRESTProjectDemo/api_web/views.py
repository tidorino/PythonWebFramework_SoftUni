from django.shortcuts import render
from rest_framework import generics as rest_views
from rest_framework import serializers
from DjangoRESTProjectDemo.api_web.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


# JSON serialization, i.e. parse models into JSON
class EmployeesListApiView(rest_views.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


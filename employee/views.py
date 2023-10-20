from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Employee
from django.views import generic

# Create your views here.
class EmployeeDetailView(generic.DetailView):
    model = Employee
    template_name = 'details.html'
from django.shortcuts import render
from employee.models import Employee
from django.views import generic


# def home(request):
#     employees: Employee[Employee] = Employee.objects.all()
#     print(employees)
#     context = {
#         'employees_list': employees,
#     }
#     return render(request, 'index.html', context=context)

class HomeView(generic.ListView):
    template_name = "index.html"
    context_object_name = "employee_list"

    def get_queryset(self):
        """
        Return the list of employees).
        """
        return Employee.objects.all()
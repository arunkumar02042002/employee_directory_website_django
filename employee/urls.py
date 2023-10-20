from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail')
]
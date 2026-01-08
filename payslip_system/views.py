from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Salary
# Create your views here.

def employee_list(request):
    employees = Employee.objects.all()
    return render(request,'employee_list.html', {'employees': employees})

def payslip_view(request, emp_id):
    employee = get_object_or_404(Employee, emp_id = emp_id)
    salary = Salary.objects.get(employee=employee)
    return render(request, 'payslip.html',{
        'employee' : employee,
        'salary' : salary
    })
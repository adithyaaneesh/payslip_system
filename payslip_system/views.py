from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm
from .models import Employee, Salary
# Create your views here.

def add_employee(request):
    if request.method == "POST":
        forms = EmployeeForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('employee_list')
    else:
        forms = EmployeeForm()
    return render(request, 'add_employee.html', {'form': forms})

def update_employee(request,emp_id):
    employee = get_object_or_404(Employee,emp_id=emp_id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form':form})

def delete_employee(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)
    employee.delete()
    return redirect('employee_list')


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
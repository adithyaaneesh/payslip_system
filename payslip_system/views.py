from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm, SalaryForm
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
    employee = get_object_or_404(Employee,id=emp_id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form':form})

def delete_employee(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    employee.delete()
    return redirect('employee_list')


def employee_list(request):
    employees = Employee.objects.all()
    return render(request,'employee_list.html', {'employees': employees})

def add_or_edit_salary(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)

    salary, created = Salary.objects.get_or_create(
        employee=employee,
        defaults={
            'hra': 0,
            'da': 0,
            'other_allowance': 0,
            'deduction': 0,
            'leave_days': 0
        }
    )

    if request.method == "POST":
        form = SalaryForm(request.POST, instance=salary)
        if form.is_valid():
            form.save()
            return redirect('payslip_view', emp_id=emp_id)
    else:
        form = SalaryForm(instance=salary)

    return render(request, 'add_salary.html', {
        'form': form,
        'employee': employee
    })

def payslip_view(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    salary = get_object_or_404(Salary, employee=employee)

    return render(request, 'payslip.html', {
        'employee': employee,
        'salary': salary
    })

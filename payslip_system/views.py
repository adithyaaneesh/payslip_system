from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm, SalaryForm
from .models import Employee, Salary
# Create your views here.

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
        return redirect('edit_employee', emp_id=employee.id)
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})



def update_employee(request, emp_id):
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
        emp_form = EmployeeForm(request.POST, instance=employee)
        sal_form = SalaryForm(request.POST, instance=salary)
        if emp_form.is_valid() and sal_form.is_valid():
            emp_form.save()
            sal_form.save()
            return redirect('employee_list')
    else:
        emp_form = EmployeeForm(instance=employee)
        sal_form = SalaryForm(instance=salary)

    return render(request, 'edit_employee.html', {
        'emp_form': emp_form,
        'sal_form': sal_form,
        'employee': employee
    })


def delete_employee(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    employee.delete()
    return redirect('employee_list')


def employee_list(request):
    employees = Employee.objects.all()
    return render(request,'employee_list.html', {'employees': employees})

def payslip_view(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    salary = get_object_or_404(Salary, employee=employee)
    return render(request, 'payslip.html', {
        'employee': employee,
        'salary': salary
    })

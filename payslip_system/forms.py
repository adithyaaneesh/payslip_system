from django import forms
from .models import Employee, Salary

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_id', 'employee_name', 'designation', 'basic_salary']

class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['hra', 'da', 'other_allowance', 'deduction', 'leave_days']
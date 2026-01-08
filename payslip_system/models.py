from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id = models.CharField(max_length=25,unique=True)
    employee_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    basic_salary = models.FloatField()

    def __str__(self):
        return self.employee_name
    

class Salary(models.Model):
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE)
    hra = models.FloatField()
    da = models.FloatField()
    other_allowance = models.FloatField()
    deduction = models.FloatField()
    leave_days = models.IntegerField(default=0)
    
    def gross_salary(self):
        gs = self.employee.basic_salary + self.hra + self.da + self.other_allowance
        return gs
    
    # def total_deduction(self):
    #     leave_deduction = (self.employee.basic_salary / 30) * self.leave_days
    #     return leave_deduction
    
    def net_salary(self):
        leave_deduction = (self.employee.basic_salary / 30) * self.leave_days
        return self.gross_salary() - self.deduction - leave_deduction


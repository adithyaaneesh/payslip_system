from django.urls import path
from . import views
urlpatterns = [
    path("employee_list",views.employee_list, name='employee_list'),
    path("payslip_view/<int:emp_id>/",views.payslip_view, name='payslip_view'),
    
]

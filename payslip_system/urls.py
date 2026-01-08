from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_employee, name='add_employee'),
    path('edit/<int:emp_id>/', views.update_employee, name='edit_employee'),
    path('delete/<int:emp_id>/', views.delete_employee, name='delete_employee'),
    path("",views.employee_list, name='employee_list'),
    path("payslip_view/<int:emp_id>/",views.payslip_view, name='payslip_view'),
    
]

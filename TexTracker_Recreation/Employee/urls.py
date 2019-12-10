from django.urls import path
from Employee.views import (
                                AdminAddEmployeeView,
                                AddEmployeePost,
                                ListEmployeePost,
                                UpdateEmployeePost,
                                EmployeePostDetailView,
                                DeleteEmployeePost
                            )

urlpatterns = [
    path('add', AdminAddEmployeeView, name='add_employee'),
    path('EmployeePost/Add',
         AddEmployeePost.as_view(), name='add_employeepost'),
    path('EmployeePost/List',
         ListEmployeePost.as_view(), name='list_employeepost'),
    path('EmployeePost/Update/<int:pk>',
         UpdateEmployeePost.as_view(), name='update_employeepost'),
    path('EmployeePost/Delete/<int:pk>',
         DeleteEmployeePost.as_view(), name='delete_employeepost'),
    path('EmployeePost/Detail/<int:pk>',
         EmployeePostDetailView.as_view(), name='detail_employeepost'),
]

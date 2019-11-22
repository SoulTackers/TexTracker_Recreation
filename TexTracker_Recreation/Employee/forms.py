from django import forms
from crispy_forms.helper import FormHelper
from Employee.models import Employee, EmployeePost


class AdminEmployeeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = Employee
        fields = [
            'employee_firstname',
            'employee_lastname',
        ]

class EmployeePostForm(forms.ModelForm):
    class Meta:
        model = EmployeePost
        fields = [
            # 'employeePost_id',
            'employeePost_details',
            'employeePost_name',
        ]

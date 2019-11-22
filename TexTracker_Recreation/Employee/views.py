from django.shortcuts import render
from django.views import View
from Employee.forms import AdminEmployeeForm, EmployeePostForm
from User.forms import CustomUserForm
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic import ListView, DetailView
from Employee.models import Employee, EmployeePost
from django.urls import reverse_lazy
# from django.models import

# Create your views here.


# def AdminAddEmployeeView(request):
#     username = models.CharField(max_length=30)
#     if request.method == 'POST':
#         if username.is_valid():  # and form1.is_valid()
#             user_form = CustomUserForm(
#                 initial={'username': username, 'password': username})
#             if user_form.is_valid()
#             user_form.save()
#             messages.add_message(
#                 request, messages.SUCCESS, 'Employee is added')
#     else:
#         form = CustomUserForm()
#     context = {
#         'form': username,
#     }
#     return render(request, 'Employee/employee.html', context)


# class EmployeeDelete(DeleteView):
#     model = Employee
#     # success_url = reverse_lazy('author-list')

class EmployeeListView(ListView):
    queryset = EmployeePost.objects.all()
    context_object_name = 'employee_list'
    paginated_by = 5


class EmployeeDetailView(DetailView):
    model = Employee


# Employee Posts...........................................................................................


# class AddEmployeePost(CreateView):
#     form_class = EmployeePostForm
#     template_name = 'Employee/EmployeePost_form.html'
#     success_url = reverse_lazy('add_employeepost')

class AddEmployeePost(CreateView):
    model = EmployeePost
    # context_object_name = 'employee_post'
    fields = [
        'employeePost_details',
        'employeePost_name',
    ]
    template_name = 'Employee/EmployeePost_form.html'
    success_url = reverse_lazy('list_employeepost')


class UpdateEmployeePost(UpdateView):
    model = EmployeePost
    fields = [
        'employeePost_details',
        'employeePost_name',
    ]
    template_name = 'Employee/EmployeePost_form.html'
    success_url = reverse_lazy('list_employeepost')
    # template_name =
    # success_url =


class DeleteEmployeePost(DeleteView):
    model = EmployeePost
    template_name = 'Employee/EmployeePost_form.html'
    success_url = reverse_lazy('list_employeepost')


class ListEmployeePost(ListView):
    queryset = EmployeePost.objects.all()
    context_object_name = 'employee_post_list123'
    paginated_by = 2
    template_name = 'Employee/EmployeePost_list.html'

class EmployeePostDetailView(DetailView):
    model = EmployeePost
    template_name = 'Employee/EmployeePost_form.html'
    context_object_name = 'employee_post_list123'

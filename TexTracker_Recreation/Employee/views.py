from django.shortcuts import render
from django.views import View
from Employee.forms import AdminEmployeeForm, EmployeePostForm
from User.forms import CustomEmployeeUserForm
from User.models import CustomUser
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic import ListView, DetailView
from Employee.models import Employee, EmployeePost
from django.urls import reverse_lazy
# from django.models import

# Create your views here.


def AdminAddEmployeeView(request):

    if request.method == 'POST':
        form = CustomEmployeeUserForm(request.POST or None)
        if form.is_valid():
            CustomUser.objects.create_user(
                    username=request.POST['user_name'],
                    first_name=request.POST['user_name'],
                    password=request.POST['user_name']
                )
            messages.add_message(
                request, messages.SUCCESS, 'Employee is added')
    else:
        form = CustomEmployeeUserForm()
    context = {
        'form': form,
    }
    return render(request, 'User/user.html', context)


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
    # def get_form(self):
    #     labels = {
    #     'employeePost_details' : 'Details',
    #     'employeePost_name' : 'Name',
    #     }
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

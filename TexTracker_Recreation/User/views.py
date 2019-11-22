from django.shortcuts import render
from User.forms import CustomUserForm
from django.views import View
from django.http import HttpResponse
from django.views.generic.edit import FormView, UpdateView, DeleteView
# Create your views here.


# class user(FormView):
#     form_class = CustomUserForm
#     template_name = 'User/user.html'
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("keyur")
#
#         return render(request, self.template_name, {'form': form})

# def user(request):
#     if request.method == 'POST':
#         form = CustomUserForm(request.POST or None)
#         # form1 = EmployeePostForm(request.POST or None)
#         if form.is_valid() :  #and form1.is_valid()
#             form.save()
#             messages.add_message(request, messages.SUCCESS, 'Employee is added')
#             form = CustomUserForm()
#             # form1.save()
#     else:
#         form = CustomUserForm()
#         # form1 = EmployeePostForm(request.POST or None)
#     context = {
#         'form' : form,
#         # 'form1' : form1
#     }
#     return render(request,'User/user.html',context)

# class UserUpdateView(UpdateView):
#     model = CustomUser
#     fields = [
#         'username','email', 'first_name', 'last_name', 'password',
#     ]
#     template_name_suffix = '_update_form'

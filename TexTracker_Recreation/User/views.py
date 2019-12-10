from django.shortcuts import render
from User.forms import UserUpdateForm, ProfileUpdateForm
from User.models import CustomUserProfile
from django.contrib import messages
from django.views import View
from django.http import HttpResponse
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

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
#             messages.add_message(request, messages.SUCCESS, 'User is added')
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

def user___(request):
    if request.method == 'POST':
        form = CustomUserAloneForm(request.POST or None)
        if form.is_valid() :
            # form.save({
            #             'username': request.POST['first_name'],
            #             'password': request.POST['first_name'],
            #         })
            messages.add_message(request, messages.SUCCESS, 'User is added')
            form = CustomUserAloneForm()
    else:
        form = CustomUserAloneForm()
    context = {
        'form' : form,
    }
    return render(request,'User/user.html',context)
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.CustomUserProfile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f'Your account has been Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=CustomUserProfile.objects.get(user = request.user))

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'User/profile.html', context)

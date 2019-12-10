from django import forms
from django.db import models
from crispy_forms.helper import FormHelper
from User.models import CustomUser, CustomUserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.form_show_labels = False

    class Meta:
        model = CustomUser

        fields = [
            'username','email', 'first_name', 'last_name', 'password1', 'password2',
        ]

        labels = {
            'username': 'User Name',
            'password1': 'Password',
            'password2': 'Confirm Password',
            'email': 'Email',
        }

class CustomEmployeeUserForm(forms.Form):
    user_name = forms.CharField(max_length=60)
    # last_name = forms.CharField(max_length=60)

    class Meta:

        fields = [
            'user_name',
        ]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'roles']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUserProfile
        fields = ['profilePic']

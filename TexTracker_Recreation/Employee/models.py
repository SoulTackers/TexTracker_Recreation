# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from User.models import CustomUser
from phone_field import PhoneField


class EmployeePost(models.Model):
    employeePost_id = models.AutoField(primary_key=True)
    employeePost_details = models.TextField(blank=True, null=True)
    employeePost_name = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.employeePost_name

    class Meta:
        managed = True
        db_table = 'employee_post'


class Employee(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    employee_id = models.AutoField(primary_key=True)
    employee_firstname = models.CharField(max_length=30, default='client')
    employee_lastname = models.CharField(max_length=30, default='')
    employee_postid = models.ForeignKey(
        EmployeePost, on_delete=models.CASCADE, blank=True, null=True)
    employee_phone = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.employee_name

    class Meta:
        managed = True
        db_table = 'employee'

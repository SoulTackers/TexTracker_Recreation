from django.contrib import admin
from User.models import CustomUser, CustomUserProfile, Role

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Role)
admin.site.register(CustomUserProfile)

from django.urls import path
from User.views import user___, profile

urlpatterns = [
        path('adduser/', user___, name='add-user'),
        path('profile/', profile, name='user-profile'),
    ]

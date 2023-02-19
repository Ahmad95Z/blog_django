from django.urls import path
from .views import *

urlpatterns = [
    path('register/',UserRegisterView.as_view(), name='register'),
    path('edit_profile/',UserEditView.as_view(), name='edit_user'),
    path('password/',ChangePasswordView.as_view()),
    path('<int:pk>/profile/',ProfileView.as_view(), name='profile_page'),
    path('<int:pk>/edit_profile_page/',ProfileEditView.as_view(), name='edit_profile_page'),
    path('create_profile/',CreateProfileView.as_view(), name='create_profile')
]
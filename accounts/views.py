from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, UpdateView, CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm, UserProfileForm 
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm 
from blog.models import Profile


class CreateProfileView(CreateView):
    model = Profile
    template_name = 'registration/create_profile.html'
    fields = ('profile_image', 'body', 'instagram_url',)
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ('profile_image', 'body', 'instagram_url',)
    success_url = reverse_lazy('index')

class ProfileView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context ['page_user'] = page_user
        return context



class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = UserProfileForm
    template_name = 'registration/edit_pofile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user



class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name='registration/change_password.html'
    success_url = reverse_lazy('index')

from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from .models import GroupProfile, Userprofile
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import RegisterViewForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class GroupProfileDetail(DetailView):
    model = GroupProfile
    template_name = 'core/groupdetail.html'
    context_object_name = 'groupprofile'
    def get_object(self):
        return GroupProfile.objects.first()
    


class UserProfileView(LoginRequiredMixin, DetailView):
    model = Userprofile
    template_name = 'core/userprofile.html'
    context_object_name = 'userprofile'
    def get_object(self):
        return self.request.user.userprofile

class UserEditor(UpdateView):
    model = Userprofile
    template_name = 'core/editor.html'
    fields = ['profile_picture','bio']
    success_url = reverse_lazy('user-profile')
    def get_object(self):
        return self.request.user.userprofile

class RegisterView(CreateView):
    form_class = RegisterViewForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('user-profile')
    def form_valid(self, form):
        new_user = form.save(commit = True)
        login(self.request, new_user)
        return super().form_valid(form)
    
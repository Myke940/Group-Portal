from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from .models import GroupProfile, Userprofile
# Create your views here.


class GroupProfileDetail(DetailView):
    model = GroupProfile
    template_name = 'core/groupdetail.html'
    context_object_name = 'groupprofile'
    def get_object(self):
        return GroupProfile.objects.first()
    


class UserProfileView(DetailView):
    model = Userprofile
    template_name = 'core/userprofile.html'
    context_object_name = 'userprofile'
    def get_object(self):
        return self.request.user.userprofile

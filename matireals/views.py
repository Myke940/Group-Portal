from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Material
from .forms import MaterialForm

# Список навчальних матеріалів
class MaterialListView(ListView):
    model = Material
    template_name = "materials/material_list.html"
    context_object_name = "materials"


# Додавання нового навчального матеріалу
class MaterialCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Material
    template_name = "materials/material_form.html"
    form_class = MaterialForm
    success_url = reverse_lazy("materials:material-list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.userprofile.role in ['instructor', 'admin']


# Оновлення існуючого матеріалу
class MaterialUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Material
    template_name = "materials/material_form.html"
    form_class = MaterialForm
    success_url = reverse_lazy("materials:material-list")

    def test_func(self):
        return self.request.user.userprofile.role in ['instructor', 'admin']


# Видалення існуючого матеріалу 
class MaterialDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Material
    template_name = "materials/material_delete_confirm.html"
    success_url = reverse_lazy("materials:material-list")

    def test_func(self):
        return self.request.user.userprofile.role in ['instructor', 'admin']
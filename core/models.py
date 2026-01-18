from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null = True, blank = True)
    roles = [('student', 'Student'), ('instructor', 'Instructor'), ('admin', 'Admin')]
    role = models.CharField(max_length = 20, choices = roles, default = 'student')
    bio = models.TextField(max_length = 500, null = True, blank = True)
    def __str__(self):
        return self.user.username

class GroupProfile(models.Model):
    name = models.CharField(max_length = 40)
    description = models.TextField()
    members = models.ManyToManyField(Userprofile)
    created_at = models.DateTimeField(auto_now_add = True)
    logo = models.ImageField(upload_to = 'group_logos/', null = True, blank = True)
    def __str__(self):
        return self.name




from django.db import models
from django.contrib.auth.models import User

class Material(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="materials/files/", null=True, blank=True)
    image = models.ImageField(upload_to="materials/images/", null=True, blank=True)
    url =  models.URLField(null=True, blank=True)
    creator =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="materials")
    created_time =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
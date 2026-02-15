from django.db import models
from django.contrib.auth.models import User

class Vote(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="votes")
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class VoteOption(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name="options")
    option_text = models.CharField(max_length=256)

    def __str__(self):
        return f"Option '{self.option_text}' from '{self.vote}' vote"


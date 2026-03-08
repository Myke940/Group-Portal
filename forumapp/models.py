from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def score(self):
        return self.votes.aggregate(models.Sum("value"))["value__sum"] or 0

    def __str__(self):
        return self.title


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="votes")
    post = models.ForeignKey(Post, related_name="votes", on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1, "Upvote"), (-1, "Downvote")])

    class Meta:
        unique_together = ("user", "post")

    def __str__(self):
        return f"{self.user.username} → {self.post.title} ({self.value})"


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"comment by: {self.user.username}"

class Message(models.Model):
    username = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['timestamp']


class Forum(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    messages = models.ManyToManyField(Message, blank = True)



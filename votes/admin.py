from django.contrib import admin
from .models import Vote, VoteOption

admin.site.register(Vote)
admin.site.register(VoteOption)
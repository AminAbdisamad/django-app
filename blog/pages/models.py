from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # models.DateTimeField(auto_now() = True) This will update date and time every time we update a post - its great for last modified field
    # models.DateTimeField(auto_add_now() = True) always presents the time post created no update
    date_posted = models.DateTimeField(default=timezone.now)
    # on_delete what happens if the User is deleted
    # on_delete = models.CASCADE if user is deleted, delete all posts from the user
    author = models.ForeignKey(User, on_delete=models.CASCADE)

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

from django.db import models
from django.conf import settings
from datetime import datetime

class Traveller(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

    def get_created_at_formatted(self):
        return self.created_at.strftime("%d/%m/%Y")

    def get_updated_at_formatted(self):
        return self.updated_at.strftime("%d/%m/%Y")

    def get_author_name(self):
        return self.author.name if self.author else 'Unknown Author'

    class Meta:
        ordering = ['-created_at']

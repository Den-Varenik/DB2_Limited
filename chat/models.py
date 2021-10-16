from django.conf import settings
from django.db import models


class Chat(models.Model):
    title = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=100)
    public = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.title)


class Message(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='messages',
                               on_delete=models.CASCADE)
    ip = models.GenericIPAddressField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    text = models.CharField(max_length=100)
    chat = models.ForeignKey(Chat, related_name="messages", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

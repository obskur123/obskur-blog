from django.db import models
import base64

from blog.storage_backends import PublicMediaStorage


class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    archived = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    anon_user = models.CharField(max_length=12)
    admin = models.BooleanField(default=False)
    content = models.CharField(max_length=512)
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.anon_user + ' ' + self.content

class DebugImage(models.Model):
    file = models.FileField(upload_to='images')
    post = models.ForeignKey(
        Post, related_name="dimages", on_delete=models.CASCADE)


class Image(models.Model):
    file = models.FileField(storage=PublicMediaStorage())
    post = models.ForeignKey(
        Post, related_name="images", on_delete=models.CASCADE)

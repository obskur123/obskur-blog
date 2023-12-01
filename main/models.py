from django.db import models
import base64


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


class Image(models.Model):
    file = models.BinaryField()
    post = models.ForeignKey(
        Post, related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return str(base64.b64encode(self.file))
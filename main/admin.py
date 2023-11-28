from django.contrib import admin
from .models import Comment, Image, Post

# Register your models here.

admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Comment)


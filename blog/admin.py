from django.contrib import admin
from blog.models import Catego, Post, Comment
# Register your models here.

admin.site.register(Catego)
admin.site.register(Post)
admin.site.register(Comment)

from django.contrib import admin
from .models import ForumUser, ForumPost, ForumComment

admin.site.register(ForumUser)
admin.site.register(ForumPost)
admin.site.register(ForumComment)

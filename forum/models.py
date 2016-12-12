from __future__ import unicode_literals

from django.db import models

class ForumUser(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    nick = models.CharField(max_length=20)
    reg_date = models.DateTimeField('Registration date', auto_now=True)

    def __str__(self):
        return "%s %s" % (self.nick, self.reg_date)

class ForumPost(models.Model):
    user = models.ForeignKey(ForumUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=9999)
    date_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s %s" % (self.user.nick, self.title, self.user.email)
    class Meta:
        ordering = ('user',)


class ForumComment(models.Model):
    user = models.ForeignKey(ForumUser, on_delete=models.CASCADE)
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    comment = models.CharField(max_length = 500)
    date_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s\n%s" % (self.user.nick, self.post.title, self.comment)
    
    class Meta:
        ordering = ('post',)


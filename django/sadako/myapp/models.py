from django.db import models

# Create your models here.
from django.utils import timezone

class signup(models.Model):
    userid = models.CharField(max_length=20, blank=true, default='')
    username = models.CharField(max_length=20, blank=true, default='')
    userpwd = models.CharField(max_length=20, blank=true, default='')
    userdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.userid

class post(models.Model):
    bbsid = models.ForeignKey('signup', on_delete = models.CASCADE)
    bbstitle = models.CharField(max_length=100, blank=True, default='')
    bbscon = models.TextField()
    bbslastdate = models.DateTimeField(auto_now=True)
    bbsfirstdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bbstitle


class comment(models.Model):
    replyid = models.ForeignKey('signup', on_delete = models.CASCADE)
    replycon = models.TextField()
    replydate = models.DateTimeField(auto_now_add=True)

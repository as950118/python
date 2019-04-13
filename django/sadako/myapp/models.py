#myapp/models.py
from django.db import models

class signup_model(models.Model):
    id = models.CharField(primary_key=True, max_length=128, default="")
    pwd = models.CharField(max_length=128, default="")
    email = models.EmailField(max_length=128, default="")
    sex = models.CharField(max_length=2, default="")
    tel = models.CharField(max_length=128, default="")
    date = models.DateTimeField(auto_now=True) #현재시각으로 자동저장

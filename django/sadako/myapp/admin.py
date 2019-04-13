#myapp/admin.py
from django.contrib import admin
# Register your models here.
from .models import signup_model
admin.site.register(signup_model)

#myapp/urls.py
from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'admin/', admin.site.urls, name='admin'),
    url(r'^$', views.main, name = 'main'),
    url(r'signup/', views.signup, name = 'signup'),
    url(r'login/', views.login, name = 'login'),
    url(r'signup_post/', views.signup_post, name = 'signup_post'),
    url(r'login_post/', views.login_post, name = 'login_post')
]

#Myapp/urls.py
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'main', views.main, name = 'main'),
    url(r'signup', views.signup, name = 'signup'),
    url(r'login', auth_views.LoginView.as_view(template_name='jhjapp/login.html'), name = 'login'),
    url(r'mypage', views.mypage, name = 'mypage'),
    url(r'bbs', views.bbs, name = 'bbs')
]

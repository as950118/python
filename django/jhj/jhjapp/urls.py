#Myapp/urls.py
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    url(r'main', views.main, name = 'main'),
    #url(r'signup', views.signup, name = 'signup'),
    url(r'signup', CreateView.as_view(template_name='jhjapp/signup.html', form_class = UserCreationForm, success_url='/login'), name = 'signup'),
    url(r'accounts/login', auth_views.LoginView.as_view(template_name='jhjapp/login.html'), name = 'login'),
    url(r'accounts/logout', auth_views.logout, {'next_page':'main'}, name = 'logout'),
    url(r'accounts/profile', views.profile, name = 'profile'),
    url(r'bbs', views.bbs, name = 'bbs')
]

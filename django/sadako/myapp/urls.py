from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'^$', views.main, name = 'main'),
    url(r'signup/', views.signup, name = 'signup'),
    url(r'login/', views.login, name = 'login'),
    url(r'mypage/', views.mypage, name = 'myapp'),
    url(r'bbs/', views.bbs, name = 'bbs'),
    url(r'gallery/', views.gallery, name = 'gallery'),
    url(r'signup_post/', views.signup_post, name = 'signup_post'),
}

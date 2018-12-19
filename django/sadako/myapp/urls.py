from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'^$', views.main, name = 'main'),
    url(r'signup/', views.board_1, name = 'signup'),
    url(r'login/', views.board_1, name = 'login'),
    url(r'mypage/', views.board_1, name = 'myapp'),
    url(r'bbs/', views.board_1, name = 'bbs'),
    url(r'gallery/', views.board_1, name = 'gallery'),
}

from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'^$', views.main, name = 'main'),
    url(r'board_1/', views.board_1, name = 'board_1'),
    url(r'board_1/', views.board_1, name = 'board_2'),
    url(r'login/', views.board_1, name = 'login'),
    url(r'logout/', views.board_1, name = 'logout'),
    url(r'signup/', views.board_1, name = 'signup')
}

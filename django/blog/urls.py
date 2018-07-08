from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'^$', views.main, name = 'main'),
    url(r'board_1/', views.board_1, name = 'board_1'),
    url(r'board_2/', views.board_2, name = 'board_2'),
    url(r'search/', views.search, name = 'search'),
    #url(r'login/', views.login, name = 'login'),
    #url(r'logout/', views.logout, name = 'logout'),
    #url(r'signup/', views.signup, name = 'signup')
}

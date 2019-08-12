from django.conf.urls import url

from . import views

urlpatterns = (
    #path('register/', views., name='register'),
    url('login/', views.login, name='login'),
    url('logout/', views.logout, name='logout'),
    url('register/', views.register, name='register'),
)
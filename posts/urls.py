from django.urls import path

from . import views

urlpatterns = [
    path('about_me/', views.about, name='about_me'),
    path('list_posts/<post_id>/detail/', views.postdetail, name='detail'),
    path('list_posts/', views.postlist, name='posts'),
    path('list_projects/', views.projectlist, name='projects'),
    #path('register/', views.Register.as_view(), name='register'),
    #path('login/', views.Login.as_view(), name='login'),
    path('', views.Posthome.as_view(), name='home'),
]


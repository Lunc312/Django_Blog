from django.urls import path

from . import views

urlpatterns = [
    path('', views.posthome, name='home'),
    path('about_me', views.about, name='about_me'),
    path('<int:post_id>/detail/', views.postdetail, name='detail'),
    path('list_posts/', views.postlist, name='posts'),
    path('list_projects/', views.projectlist, name='projects'),
]


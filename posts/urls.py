from django.urls import path

from . import views

urlpatterns = [
    path('about_me/', views.about, name='about_me'),
    path('list_posts/addcomment/<post_id>/', views.addcomment, name='addcomment'),
    path('list_posts/detail/<post_id>/', views.postdetail, name='detail'),
    path('list_posts/all', views.postlist, name='posts'),
    path('list_projects/', views.projectlist, name='projects'),
    path('page_posts/<page_number>/', views.postlist, name='posts'),
    path('page_projects/<page_number>/', views.projectlist, name='projects'),
    path('', views.posthome, name='home'),
]


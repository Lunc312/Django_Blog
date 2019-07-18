from django.urls import path

from . import views

urlpatterns = [
    path('', views.posthome, name='home'),
    path('/create/', views.postcreate, name='create'),
    path('<int:post_id>/detail/', views.postdetail, name='detail'),
    path('list/', views.postlist, name='list'),
    path('<int:post_id>/update/', views.postupdate, name='update'),
    path('<int:post_id>/delete/', views.postdelete, name='delete'),
]


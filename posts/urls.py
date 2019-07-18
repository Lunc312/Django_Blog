from django.urls import path

from . import views

urlpatterns = [
    path('', views.posthome, name='home'),
    path('create/', views.postcreate, name='create'),
    path('detail/', views.postdetail, name='detail'),
    path('list/', views.postlist, name='list'),
    path('update/', views.postupdate, name='update'),
    path('delete/', views.postdelete, name='delete'),
]


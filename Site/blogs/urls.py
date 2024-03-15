from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main, name='Main'),
    path('SignUp/', views.SignUp, name='SignUp'),
    path('SignIn/', views.SignIn, name='SignIn'),
    #path('dashboard/<int:id>/', views.dasboard, name='dashboard')
    path('dashboard/', views.dasboard, name='dashboard'),
    path('dashboard/Logout', views.Logout, name='Logout'),
    path('dashboard/addPost/<int:id>/', views.addPost, name='addPost'),
    path('dashboard/delete_post/<int:id>/', views.deletePost, name='delete_post'),
    path('dashboard/update_post/<int:post_id>/', views.updatePost, name='update_post')
]
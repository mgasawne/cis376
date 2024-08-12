from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profiles/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('create-post/', views.create_post, name='create_post'),
    path('delete-post/<int:pk>/', views.delete_post, name='delete_post'),
    path('edit-post/<int:pk>/', views.edit_post, name='edit_post'),
    path('comment-post/<int:pk>/', views.comment_post, name='comment_post'),
]

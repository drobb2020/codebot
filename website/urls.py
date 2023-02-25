from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suggest/', views.suggest, name='suggest'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]

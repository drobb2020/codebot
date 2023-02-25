from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suggest/', views.suggest, name='suggest'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('past_code/', views.past_code, name='past_code'),
    path('delete_past_code/<past_id>/', views.delete_past_code, name='delete_past'),
]

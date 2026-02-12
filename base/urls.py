from django.urls import path
from base import views

app_name = 'base'

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
]
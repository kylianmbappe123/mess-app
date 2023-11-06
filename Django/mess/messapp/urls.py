from django.urls import path
from . import views
  
  
urlpatterns=[
    path('',views.index,name='index'),
    path('user_register',views.user_register,name='user_register'),
    path('user_login',views.user_login,name='user_login'),
    path('user_home',views.user_home,name='user_home'),
    path('sign_out',views.sign_out,name='sign_out'),
    path('mess_register',views.mess_register,name='mess_register'),
    path('mess_login',views.mess_login,name='mess_login'),
    path('mess_home',views.mess_home,name='mess_home'),
]
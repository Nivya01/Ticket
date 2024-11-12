from django.urls import path
from .views import *

urlpatterns = [
    
    path('admin_register/', AdminRegisterView.as_view(), name='Admin_Register'),
    path('admin_login/',AdminLoginView.as_view(), name='Admin_Login'),

    path('user_register/', UserRegisterView.as_view(), name='User_Register'),
    path('user_login/', UserLoginView.as_view(), name='User_Login'),
    
    path('logout/', ActiveUserLogoutView.as_view(), name='ActiveUser_Logout'),
]

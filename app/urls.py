from django.urls import path
from .views import UserRegistrationApi, UserLoginApi, UserLogoutApi

urlpatterns = [
    path('register/', UserRegistrationApi.as_view(), name='user_register_api'),
    path('login/', UserLoginApi.as_view(), name='user_login_api'),
    path('logout/', UserLogoutApi.as_view(), name='user_logout_api'),
]

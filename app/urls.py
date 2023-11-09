from django.urls import path
from .views import UserRegistrationApi, UserLoginApi, UserLogoutApi, UserProfileApi

urlpatterns = [
    path('register/', UserRegistrationApi.as_view(), name='user_register_api'),
    path('login/', UserLoginApi.as_view(), name='user_login_api'),
    path('logout/', UserLogoutApi.as_view(), name='user_logout_api'), # this is not working, maybe some logic
    path('profile/', UserProfileApi.as_view(), name='user-profile'), # this is not working, maybe some logic
]

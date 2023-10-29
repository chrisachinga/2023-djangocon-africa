from django.urls import path
from .views import MentorSignUpView, MenteeSignUpView, login_view

app_name = 'app'
urlpatterns = [
    path('signup/mentor/', MentorSignUpView.as_view(), name='mentor_signup'),
    path('signup/mentee/', MenteeSignUpView.as_view(), name='mentee_signup'),
    path('login/', login_view, name='login'),
]

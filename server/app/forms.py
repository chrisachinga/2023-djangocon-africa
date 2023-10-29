from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, MentorProfile, MenteeProfile, Education, WorkExperience, Skill

class MentorSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'gender', 'year_of_birth', 'bio']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'Mentor'
        if commit:
            user.save()
            MentorProfile.objects.create(user=user)
        return user

class MenteeSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'gender', 'year_of_birth', 'bio']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'Mentee'
        if commit:
            user.save()
            MenteeProfile.objects.create(user=user)
        return user

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

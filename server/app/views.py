from django.urls import reverse_lazy
from django.views import generic
from app.forms import MentorSignUpForm, MenteeSignUpForm, UserLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

class MentorSignUpView(generic.CreateView):
    form_class = MentorSignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup_mentor.html"

class MenteeSignUpView(generic.CreateView):
    form_class = MenteeSignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup_mentee.html"

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('some_view_name')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

User = get_user_model()




def signup_user(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'authentication/register.html', {'error': 'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], email=request.POST['email'],
                                                password=request.POST['password1'])
                auth.login(request, user)
                return redirect('authentication:log_in')
        else:
            return render(request, 'authentication/register.html', {'error': 'Password does not match!'})
    else:
        return render(request, 'authentication/register.html')


def login_user(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'authentication/login.html', {'error': 'Username or password is incorrect!'})
    else:
        return render(request, 'authentication/login.html')


@login_required
def logout_user(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('authentication:log_in')


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'authentication/password_reset.html'
    email_template_name = 'authentication/password_reset_email.html'
    subject_template_name = 'authentication/password_reset_subject'
    success_url = reverse_lazy("authentication:password_reset_sent")


def password_reset_sent(request):
    return render(request, "authentication/password_reset_sent.html", {})







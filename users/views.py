from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(
            data=request.POST
        )
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(
                username=username,
                password=password
            )
            if user:
                auth.login(
                    request=request,
                    user=user
                )
                return HttpResponseRedirect(
                    redirect_to=reverse(
                        viewname='index'
                    )
                )
    else:
        form = UserLoginForm()
    context: dict = {
        'form': form
    }
    return render(
        request=request,
        template_name='users/login.html',
        context=context,
    )


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(
            data=request.POST
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('users:login')
            )
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(
        request=request,
        template_name='users/registration.html',
        context=context
    )


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('users:profile')
            )
        else:
            print(form.errors)
    else:
        form = UserProfileForm(
            instance=request.user
        )
    context = {
        'title': 'Store профиль',
        'form': form
    }
    return render(
        request=request,
        template_name='users/profile.html',
        context=context
    )

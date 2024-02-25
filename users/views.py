from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from users.models import User
from users.forms import UserLoginForm
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
    return render(
        request=request,
        template_name='users/registration.html'
    )

from django.shortcuts import render


def login(request):
    return render(
        request=request,
        template_name='users/login.html'
    )


def registration(request):
    return render(
        request=request,
        template_name='users/registration.html'
    )

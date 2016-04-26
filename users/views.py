from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render
from users.models import User


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email.lower())
        except Exception as e:
            return redirect(settings.LOGIN_URL)

        user = authenticate(username=user.username, password=password)

        if not user:
            return redirect(settings.LOGIN_URL)

        if not user.is_active:
            return redirect(settings.LOGIN_URL)

        login(request, user)

        if request.POST.get('next', None):
            return redirect(request.POST['next'])

        return redirect(settings.LOGIN_REDIRECT_URL)

    context = {}
    if request.GET.get('next', None):
        context['next'] = request.GET['next']

    return render(request, 'auth/login.html', context=context)


def user_logout(request):
    logout(request)
    return redirect(settings.LOGIN_URL)

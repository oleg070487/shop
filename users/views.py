from django.shortcuts import render


def login(request):
    context = {
        'title': 'ETEHNO - Авторизация'
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'ETEHNO - Регистрация'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'ETEHNO - Кабинет'
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    ...
    # context = {
    #     'title': 'ETEHNO - Выход'
    # }
    # return render(request, 'users/logout.html', context)

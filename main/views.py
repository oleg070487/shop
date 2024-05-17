from django.shortcuts import render


def index(request):
    context = {
        "title": "ETEHNO - Главная",
        "content": "Магазин электроники ETEHNO",
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "ETEHNO - О нас",
        "content": "О нас",
        "text_on_page": "Текст о том какой крутой магазин!",
    }
    return render(request, "main/about.html", context)

from django.shortcuts import render

from goods.models import Categories


def index(request):
    categories = Categories.objects.all()
    context = {
        "title": "ETEHNO - Главная",
        "content": "Магазин электроники ETEHNO",
        "categories": categories,
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "ETEHNO - О нас",
        "content": "О нас",
        "text_on_page": "Текст о том какой крутой магазин!",
    }
    return render(request, "main/about.html", context)

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse


def posthome(request):
    content={
        "title": "Домашняя страница"
    }
    return render(request, "posts/index.html", content)


def postcreate(request):
    content = {
        "title": "Создание"
    }
    return render(request, "posts/index.html", content)


def postdetail(request):
    content = {
        "title": "Страница"
    }
    return render(request, "posts/index.html", content)


def postlist(request):
    content = {
        "title": "Список страниц"
    }
    return render(request, "posts/index.html", content)


def postupdate(request):
    content = {
        "title": "Редактирование страницы"
    }
    return render(request, "posts/index.html", content)


def postdelete(request):
    content = {
        "title": "Удаление страницы"
    }
    return render(request, "posts/index.html", content)




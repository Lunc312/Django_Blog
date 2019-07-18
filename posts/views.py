from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from posts.models import Post


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


def postdetail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    content = {
        "title": post.title,
        'post': post,
    }
    return render(request, "posts/detail.html", content)


def postlist(request):
    posts = Post.objects.all()
    content = {
        "title": "Список страниц",
        "posts": posts,
    }
    return render(request, "posts/list.html", content)


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




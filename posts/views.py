from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from posts.models import Post, Project


def posthome(request):
    content={
        "title": "Домашняя страница"
    }
    return render(request, "posts/index.html", content)


def about(request):
    content = {
        "title": "О себе"
    }
    return render(request, "posts/about.html", content)


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
        "title": "Блог",
        "posts": posts,
    }
    return render(request, "posts/list_posts.html", content)


def projectlist(request):
    projects = Project.objects.all()
    content = {
        "title": "Мои проекты",
        'projects': projects,
    }
    return render(request, "posts/list_projects.html", content)





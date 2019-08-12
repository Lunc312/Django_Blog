from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from .forms import CommentsForm
from django.template.context_processors import csrf
from django.contrib import auth

from posts.models import Post, Project, Human, Comments


def posthome(request):
    content = {
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
    comments = Comments.objects.filter(comments_post_id=post_id)
    form = CommentsForm
    content = {}
    content.update(csrf(request))
    content = {
        'title': post.title,
        'post': post,
        'comments': comments,
        'form': form,
        'username': auth.get_user(request).username,
    }
    return render(request,"posts/detail.html", content)


def addcomment(request, post_id):
    if request.POST:
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_posts = Post.objects.get(id=post_id)
            form.save()
    return redirect('/list_posts/addcomment/%s/' % post_id)


def postlist(request):
    posts = Post.objects.all()
    content = {
        "title": "Блог",
        "posts": posts,
        'username': auth.get_user(request).username
    }
    return render(request, "posts/list_posts.html", content)


def projectlist(request):
    projects = Project.objects.all()
    content = {
        "title": "Мои проекты",
        'projects': projects,
    }
    return render(request, "posts/list_projects.html", content)





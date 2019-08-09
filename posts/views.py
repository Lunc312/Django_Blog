from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from posts.models import Post, Project, Human, Comments


class Posthome(TemplateView):

    content = {
        "title": "Домашняя страница"
    }

    def get(self, request):
        if request.user.is_authenticated:
            humans = Human.objects.all()
            ctx ={}
            ctx['humans'] = humans
            return render(request, "posts/index.html", self.content, ctx)
        else:
            return render(request, "posts/index.html", self.content, {})


def about(request):
    content = {
        "title": "О себе"
    }
    return render(request, "posts/about.html", content)


def postdetail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comments.objects.filter(comments_post_id=post_id)
    content = {
        "title": post.title,
        'post': post,
        'comments': comments
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





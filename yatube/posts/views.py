from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from yatube.settings import QTY_POSTS_PAGE

# Create your views here.


def index(request):
    template = 'posts/index.html/'
    posts = posts = Post.objects.all()[:QTY_POSTS_PAGE]
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html/'
    posts = group.posts.all()[:QTY_POSTS_PAGE]
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
#    return HttpResponse(f'А это невьебенный пост от нашего блогера {sl}')

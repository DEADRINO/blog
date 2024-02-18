from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .pagination import get_paginated_objects


def posts(request):
    posts_list = Post.objects.all()
    pagination = get_paginated_objects(request, posts_list, 10)
    context = {
        'pagination': pagination
    }
    return render(request,
                  'posts/posts.html',
                  context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.read = True
    post.save()
    context = {
        'post': post
    }
    return render(request,
                  'posts/post_detail.html',
                  context)


def personal_feed(request):
    posts_list = Post.objects.filter(author__following__user=request.user)\
                             .order_by('-date_added')
    pagination = get_paginated_objects(request, posts_list, 10)
    context = {
        'pagination': pagination
    }
    return render(request,
                  'posts/personal_feed.html',
                  context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    post_list = author.posts.all()
    is_auth = request.user.is_authenticated
    following = is_auth and author.following.filter(user=request.user).exists()
    paginator = get_paginated_objects(request, post_list, 10)
    context = {
        'paginator': paginator,
        'author': author,
        'following': following
    }
    return render(request, 'posts/profile.html', context)


@login_required
def profile_follow(request, username):
    author = get_object_or_404(User, username=username)
    if (author != request.user
        and not Follow.objects.filter(user=request.user,
                                      author=author).exists()):
        Follow.objects.create(
            user=request.user,
            author=author,
        )
    return redirect('posts:profile', username=username)


@login_required
def profile_unfollow(request, username):
    get_object_or_404(Follow, user=request.user,
                      author__username=username).delete()
    return redirect('posts:profile', username=username)
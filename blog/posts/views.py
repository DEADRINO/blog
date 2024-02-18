from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .pagination import get_paginated_objects


def posts(request):
    posts_list = Post.objects.all()
    pagination = get_paginated_objects(request, posts_list, 10)

    return render(request,
                  'posts/posts.html',
                  {'pagination': pagination})



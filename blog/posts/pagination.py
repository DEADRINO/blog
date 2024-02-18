from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def get_paginated_objects(request, objects, num_per_page):
    paginator = Paginator(objects, num_per_page)
    page = request.GET.get('page', 1)
    try:
        paginated_objects = paginator.page(page)
    except PageNotAnInteger:
        paginated_objects = paginator.page(1)
    except EmptyPage:
        paginated_objects = paginator.page(paginator.num_pages)
    return paginated_objects

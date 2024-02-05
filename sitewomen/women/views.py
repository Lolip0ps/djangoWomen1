from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the")


def category(request, cat_id):
    return HttpResponse(f'<h1>Category</h1><p>id: {cat_id}</p>')


def category_by_slug(request, cat_slug):
    print(request.GET)
    return HttpResponse(f'<h1>Category by slug</h1><p>slug: {cat_slug}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound(f'Страница не найдена {exception}')

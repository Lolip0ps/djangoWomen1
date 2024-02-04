from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the")


def category(request, cat_id):
    return HttpResponse(f'<h1>Category</h1><p>id: {cat_id}</p>')


def category_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Category by slug</h1><p>slug: {cat_slug}</p>')

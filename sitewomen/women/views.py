from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)

    data = {
        'title': 'Главная страница',
        'menu': menu,
        'float': 12.765,
        'str': 'sdfsd',

    }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'О нас'})


def category(request, cat_id):
    return HttpResponse(f'<h1>Category</h1><p>id: {cat_id}</p>')


def category_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Category by slug</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    if year > 2024:
        uri = reverse('cats', args=('music',))
        return HttpResponseRedirect(uri)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

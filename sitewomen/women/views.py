from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'addpage'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'Боба', 'content': 'Биография бобы', "is_published": True},
    {'id': 2, 'title': 'Биба', 'content': 'Биография Бибы', "is_published": False},
    {'id': 3, 'title': 'Пупа', 'content': 'Биография Пупы', "is_published": True},
]


def index(request):
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)

    data = {
        'posts': data_db,
        'title': 'Главная страница',
        'menu': menu,
        'float': 12.765,
        'str': 'sdfsd',

    }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'О нас'})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')

"""Views file."""
from django.http import HttpResponse


def index(request):
    """Индекс."""
    return HttpResponse('У меня получилось!')


def second_page(request):
    """Вторая страница."""
    return HttpResponse('А это вторая страница')

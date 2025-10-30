from django.shortcuts import render


def index(request):
    context = {
        'app_name': 'Приложение: Список Статей (article)',
        'page_title': 'Главная страница приложения статей',
    }
    return render(request, 'article/index.html', context=context)
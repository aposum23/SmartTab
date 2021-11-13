from django.shortcuts import render


def todo_list(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    data = {"title": "Список дел",
            "text": "Главная страница",
            "buttons_name": [
                'todo_list',
                'edit',
                'friends',
                'share',
                'settings'
            ]}
    return render(
        request,
        'index.html',
        context=data,
    )


def edit(request):
    """
    Функция отображения для редактора списка дел.
    """
    data = {"title": "Редактировать список дел",
            "text": "Редактировать список дел",
            "buttons_name": [
                'todo_list',
                'friends',
                'share',
                'settings'
            ]}
    return render(
        request,
        'index.html',
        context=data,
    )


def friends(request):
    """
    Функция отображения для писка друзей.
    """
    data = {"title": "Список друзей",
            "text": "Список друзей",
            "buttons_name": [
                'todo_list',
                'edit',
                'share',
                'settings'
            ]}
    return render(
        request,
        'index.html',
        context=data,
    )


def share(request):
    """
    Функция отображения для страницы с возможность отправить список дела в соц сети.
    """
    data = {"title": "Поделиться списком",
            "text": "Поделиться списком",
            "buttons_name": [
                'todo_list',
                'edit',
                'friends',
                'settings'
            ]}
    return render(
        request,
        'index.html',
        context=data,
    )


def settings(request):
    """
    Функция отображения для окна настроек.
    """
    data = {"title": "Настройки",
            "text": "Тут будут настройки",
            "buttons_name": [
                'todo_list',
                'edit',
                'friends',
                'share',
            ]}
    return render(
        request,
        'index.html',
        context=data,
    )


def authorization(request):
    """
    Функция отображения для окна авторизации.
    """
    data = {"title": "Войти",
            "text": "Тут будет окно входа",
            "buttons_name": [
                'todo_list',
            ]}
    return render(
        request,
        'index.html',
        context=data,
    )

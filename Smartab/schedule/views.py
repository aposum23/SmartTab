from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def todo_list(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    u = request.user
    if u.is_authenticated:
        data = {"title": "Список дел",
                "status": u.is_authenticated,
                "text": "Главная страница",
                "buttons_name": [
                    'todo_list',
                    'edit',
                    'friends',
                    'share',
                    'settings',
                    'logout',
                ]}
        return render(
            request,
            'index.html',
            context=data,
        )
    else:
        return redirect('./authorization')


def edit(request):
    """
    Функция отображения для редактора списка дел.
    """
    u = request.user
    if u.is_authenticated:
        data = {"title": "Редактировать список дел",
                "status": u.is_authenticated,
                "text": "Редактировать список дел",
                "buttons_name": [
                    'todo_list',
                    'friends',
                    'share',
                    'settings',
                ]}
        return render(
            request,
            'index.html',
            context=data,
        )
    else:
        return redirect('./authorization')


def friends(request):
    """
    Функция отображения для писка друзей.
    """
    u = request.user
    if u.is_authenticated:
        data = {"title": "Список друзей",
                "status": u.is_authenticated,
                "text": "Список друзей",
                "buttons_name": [
                    'todo_list',
                    'edit',
                    'share',
                    'settings',
                ]}
        return render(
            request,
            'index.html',
            context=data,
        )
    else:
        return redirect('./authorization')


def share(request):
    """
    Функция отображения для страницы с возможность отправить список дела в соц сети.
    """
    u = request.user
    if u.is_authenticated:
        data = {"title": "Поделиться списком",
                "status": u.is_authenticated,
                "text": "Поделиться списком",
                "buttons_name": [
                    'todo_list',
                    'edit',
                    'friends',
                    'settings',
                ]}
        return render(
            request,
            'index.html',
            context=data,
        )
    else:
        return redirect('./authorization')


def settings(request):
    """
    Функция отображения для окна настроек.
    """
    u = request.user
    if u.is_authenticated:
        data = {"title": "Настройки",
                "status": u.is_authenticated,
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
    else:
        return redirect('./authorization')


def authorization(request):
    """
    Функция отображения для окна авторизации.
    """
    u = request.user
    if u.is_authenticated:
        return redirect('./todo_list')
    else:
        request_text = str(request)
        if 'registration' in request_text:
            if request.method == "POST":
                username = request.POST.get("username")
                password = request.POST.get("password")
                first_name = request.POST.get("first_name")
                last_name = request.POST.get("last_name")
                email = request.POST.get("email")

                names = get_user_model()
                names = list(names.objects.all())

                for name in names:
                    if username in str(name):
                        form = RegisterForm()
                        data = {"title": "Войти",
                                "form": form,
                                "status": u.is_authenticated,
                                "text": "Пользователь с таким логином уже существует",
                                }
                        return render(
                            request,
                            'registration.html',
                            context=data,
                        )
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/schedule/')
                return redirect('/schedule/')
            else:
                form = RegisterForm()
                data = {"title": "Войти",
                        "form": form,
                        "status": u.is_authenticated,
                        "text": "Введите данные для регистрации",
                        }
                return render(
                    request,
                    'registration.html',
                    context=data,
                )

        if 'login' in request_text:
            if request.method == "POST":
                username = request.POST.get("username")
                password = request.POST.get("password")
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/schedule/')
                else:
                    form = LoginForm()
                    data = {"title": "Войти",
                            "form": form,
                            "status": u.is_authenticated,
                            "text": "Неверный логин или пароль",
                            }
                    return render(
                        request,
                        'login.html',
                        context=data,
                    )
            else:
                form = LoginForm()
                data = {"title": "Войти",
                        "form": form,
                        "status": u.is_authenticated,
                        "text": "Введите данные для вход",
                        }
                return render(
                    request,
                    'login.html',
                    context=data,
                )
        else:
            data = {"title": "Войти",
                    "status": auth.get_user(request).is_authenticated,
                    "text": "default",
                    "buttons_name": [
                        'login',
                        'registration'
                    ]}
            return render(
                request,
                'index.html',
                context=data,
            )


def logout_view(request):
    u = request.user
    if u.is_authenticated:
        logout(request)
    return redirect('./authorization')

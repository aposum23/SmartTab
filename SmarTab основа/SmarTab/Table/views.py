from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from datetime import datetime
from .forms import *
from django.core.files.storage import FileSystemStorage


#---------------Духно Михаил Александрович------------
def table_today(request):
    today = timezone.now()
    usr = request.user
    tasks = Task.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day, username=usr)
    try:
        opt = UserOptions.objects.get(usr=usr).order_by("-id")
        print(opt)
        img = opt.usr_img
        perems = {'tasks': tasks, 'first_name': usr.first_name, 'last_name': usr.last_name, 'img': img}
    except:
        perems = {'tasks': tasks, 'first_name': usr.first_name, 'last_name': usr.last_name, 'img': ''}
        print("error")
    return render(request, 'shedule.html', perems)


def add_to_shad(request):
    name = request.POST.get('head')
    desc = request.POST.get('desc')
    coords1 = request.POST.get('crds1')
    coords2 = request.POST.get('crds2')
    date = request.POST.get('date')
    usr = request.user
    if coords1 != None and coords2 != None:
        Task.objects.create(name=name, desc=desc, date=datetime.strptime(date, "%Y-%m-%d"), coords=coords1 + ';' + coords2, username=usr)
    try:
        opt = UserOptions.objects.latest(usr=usr)
        img = opt.usr_img
        perems = {'first_name': usr.first_name, 'last_name': usr.last_name, 'img': img}
    except:
        perems = {'first_name': usr.first_name, 'last_name': usr.last_name, 'img': ''}
    return render(request, 'add_to_shedule.html', perems)


class auth(LoginView):
    form_class = AuthUserForm
    template_name = 'auth.html'


class registr(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration.html'
    success_url = reverse_lazy('Table:auth-page')


def options(request):
    img = request.POST.get('img')
    usr = request.user
    if request.method == 'POST':
        file = request.FILES[img]
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)
        UserOptions.objects.create(usr=usr, usr_img=img)
    try:
        opt = UserOptions.objects.latest(usr=usr)
        img = opt.usr_img
        perems = {'first_name': usr.first_name, 'last_name': usr.last_name, 'img': img}
    except:
        perems = {'first_name': usr.first_name, 'last_name': usr.last_name, 'img': ''}
    return render(request, 'options.html', perems)
#----------misha.duhno@mail.ru---------------
from django.urls import path
from . import views


urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('edit', views.edit, name='edit'),
    path('friends', views.friends, name='friends'),
    path('share', views.share, name='share'),
    path('settings', views.settings, name='settings'),
    path('authorization', views.authorization, name='authorization'),
    path('authorization/login', views.authorization, name='login'),
    path('authorization/registration', views.authorization, name='registration'),
    path('logout', views.logout_view, name='logout')
]

from django.urls import path
from . import views


#---------------Духно Михаил Александрович------------
app_name = 'Table'

urlpatterns = [
    path('table', views.table_today, name='table-today'),
    path('add-to-shadule', views.add_to_shad, name='add-to-shad'),
    path('', views.auth.as_view(), name='auth-page'),
    path('registration', views.registr.as_view(), name='registration-page'),
    path('options', views.options, name='options'),
]
#----------misha.duhno@mail.ru---------------
from django.urls import path
from . import views

app_name = 'kunjungan'
urlpatterns = [
    path('', views.form_pengunjung, name='index'),
]

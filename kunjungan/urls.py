from django.urls import path
from . import views

app_name = 'kunjungan'
urlpatterns = [
    path('', views.form_pengunjung, name='index'),
    path('/csv', views.laporan_csv, name='laporan_csv'),
]

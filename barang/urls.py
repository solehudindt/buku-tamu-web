from django.views.generic.base import TemplateView
from django.urls import path
from . import views

app_name = 'barang'
urlpatterns = [
    path('', views.viewPinjam, name='index'),
    path('peminjaman', views.peminjaman, name='peminjaman'),
    path('penitipan', views.penitipan, name='penitipan'),
    path('actionUrl/<int:barang_id>', views.pengembalian, name='pengembalian'),
]

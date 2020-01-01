from django.views.generic.base import TemplateView
from django.urls import path
from . import views

app_name = 'barang'
urlpatterns = [
    path('', views.viewBarang, name='index'),
    path('adm_brg', views.titipPinjam, name='titipPinjam'),
    path('actionUrl/<int:barang_id>', views.pungutPengembalian, name='pgtPengembalian'),
]

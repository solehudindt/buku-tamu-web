from django.views.generic.base import TemplateView
from django.urls import path
from . import views

app_name = 'barang'
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('peminjaman', views.peminjaman, name='peminjaman'),
]

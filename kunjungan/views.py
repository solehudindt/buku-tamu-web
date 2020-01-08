from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormPengunjung
from .admin import Pengunjung
from barang.admin import export_csv
from django.http import HttpResponse

def index(request):
    return HttpResponse("Ok")

def laporan_csv(request):
    queryset = Pengunjung.objects.all()

    return export_csv(request, queryset)

def form_pengunjung(request):
    if request.method == 'POST':
        form = FormPengunjung(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success, Terimakasih sudah mengisi Buku Tamu')

            return redirect('kunjungan:index')
        else:
            messages.error(request, 'Error, Terjadi kesalahan')
    else:
        form = FormPengunjung()

    return render(request, 'kunjungan/form_pengunjung.html', {'form':form, 'header':'Form Buku Tamu'})
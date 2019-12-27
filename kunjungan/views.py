from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormPengunjung
from django.http import HttpResponse

def index(request):
    return HttpResponse("sadklk")

def form_pengunjung(request):
    if request.method == 'POST':
        form = FormPengunjung(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success')

            return redirect('kunjungan:index')
        else:
            messages.error(request, 'Error')
    else:
        form = FormPengunjung()

    return render(request, 'kunjungan/form_pengunjung.html', {'form':form, 'header':'Form Buku Tamu'})
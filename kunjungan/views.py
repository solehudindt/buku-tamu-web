from django.shortcuts import render
from .forms import FormPengunjung
from django.http import HttpResponse

def index(request):
    return HttpResponse("sadklk")

def form_pengunjung(request):
    if request.method == 'POST':
        form = FormPengunjung(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = FormPengunjung()
    return render(request, 'kunjungan/form_pengunjung.html', {'form':form})
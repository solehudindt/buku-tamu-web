from django.shortcuts import render, redirect
from .forms import FormPeminjaman
from .models import Peminjaman
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def viewPinjam(request):
    list_pinjam = Peminjaman.objects.all()

    return render(request, 'barang/dashboard_brg.html', {'pinjaman':list_pinjam})

def peminjaman(request):
    if request.method == 'POST':
        form = FormPeminjaman(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success')

            return redirect('peminjaman:index')
        else:
            messages.error(request, 'Error')
    else:
        form = FormPeminjaman()
        print("Bukan POST")
    return render(request, 'barang/form_pinjam.html', {'header':'Peminjaman', 'form':form})

def penitipan(request):
    return render(request, 'barang/form_nitip.html', {'header':'Penitipan'})
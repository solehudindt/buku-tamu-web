from django.shortcuts import render, redirect
from .forms import FormBrg
from .models import AdmBarang
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def viewBarang(request):
    list_brg = AdmBarang.objects.all()

    return render(request, 'barang/dashboard_brg.html', {'barangs':list_brg, 'header':'Daftar Barang'})

def pungutPengembalian(request, barang_id):
    AdmBarang.objects.filter(id=barang_id).update(status=True)
    
    return redirect('barang:index')

def titipPinjam(request):
    if request.method == 'POST':
        form = FormBrg(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success')

            return redirect('barang:index')
        else:
            messages.error(request, 'Error')
    else:
        form = FormBrg()
        print("Bukan POST")
    return render(request, 'barang/form_brg.html', {'header':'Peminjaman / Penitipan', 'form':form})
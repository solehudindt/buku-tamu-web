from django.shortcuts import render, redirect
from .forms import FormBrg
from .models import AdmBarang
import csv
from django.utils.encoding import smart_str
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def laporan_csv(request):
    queryset = AdmBarang.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=laporan_bukutamu.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Nama"),
        smart_str(u"Angkatan"),
        smart_str(u"Barang"),
        smart_str(u"Tanggal"),
        smart_str(u"Jenis"),
        smart_str(u"Status"),
        
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.nama),
            smart_str(obj.angkatan),
            smart_str(obj.barang),
            smart_str(obj.tanggal),
            smart_str(obj.jenis),
            smart_str(obj.status),
        ])
    return response

def viewBarang(request):
    list_brg = AdmBarang.objects.all()

    return render(request, 'barang/dashboard_brg.html', {'barangs':list_brg, 'header':'Daftar Barang'})

def pungutPengembalian(request, barang_id):
    try:
        AdmBarang.objects.filter(id=barang_id).update(status=True)

        messages.success(request, 'Pengembalian/Pengambilan Berhasil')
    except:
        messages.error(request, 'Error, Terjadi kesalahan')
    
    return redirect('barang:index')

def titipPinjam(request):
    if request.method == 'POST':
        form = FormBrg(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success, Peminjaman/Penitipan Berhasil')

            return redirect('barang:titipPinjam')
        else:
            messages.error(request, 'Error, Terjadi kesalahan')
    else:
        form = FormBrg()
        print("Bukan POST")
    return render(request, 'barang/form_brg.html', {'header':'Peminjaman / Penitipan', 'form':form})
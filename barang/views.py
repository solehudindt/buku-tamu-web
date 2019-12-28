from django.shortcuts import render

# Create your views here.

def peminjaman(request):
    return render(request, 'barang/form_pinjam.html', {'header':'Peminjaman'})
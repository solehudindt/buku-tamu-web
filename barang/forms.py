from django import forms
from .models import Peminjaman

class FormPeminjaman(forms.ModelForm):
    class Meta:
        model = Peminjaman
        fields = ('nama', 'barang')

        labels = {
            'nama': 'Nama Peminjam',
            'barang': 'Nama Barang',
        }
        
        widgets = {
            # 'tanggal': forms.DateInput(format=('dd/mm/yyy'), attrs={'class':'form-control', 'placeholder':'Pilih tanggal', 'type':'date'}),
            'nama': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Masukan nama anda'}),
            'barang': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Masukan nama barang'}),
        }

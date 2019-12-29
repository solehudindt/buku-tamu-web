from django import forms
from .models import Peminjaman

class FormPeminjaman(forms.ModelForm):
    class Meta():
        model = Peminjaman
        fields = ('nama','barang')

        labels = {
            'nama': 'Nama Peminjam',
            'barang': 'Nama Barang',
        }
        
        widgets = {
            # 'tanggal': forms.DateInput(attrs={'class':'form-control',
            #                                     'placeholder':'Pilih tanggal',
            #                                     'type':'date'
            #                                 }),
            'nama': forms.TextInput(attrs={'class':'form-control'}),
            'barang': forms.TextInput(attrs={'class':'form-control'}),
        }

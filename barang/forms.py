from django import forms
from .models import AdmBarang
import datetime

def year_choices():
    return [(r,r) for r in range(2010, datetime.date.today().year+1)]

class FormBrg(forms.ModelForm):
    class Meta():
        model = AdmBarang
        fields = ('nama', 'angkatan','barang', 'jenis')

        labels = {
            'nama': 'Nama Peminjam',
            'barang': 'Nama Barang',
        }
        
        widgets = {
            'nama': forms.TextInput(attrs={'class':'form-control'}),
            'angkatan': forms.Select(choices=year_choices(), attrs={'class':'form-control'}),
            'barang': forms.TextInput(attrs={'class':'form-control'}),
            'jenis': forms.Select(attrs={'class':'form-control'}),
        }

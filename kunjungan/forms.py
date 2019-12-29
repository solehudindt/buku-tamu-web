from django import forms
from .models import Pengunjung
import datetime

def year_choices():
    return [(r,r) for r in range(2010, datetime.date.today().year+1)]

class FormPengunjung(forms.ModelForm):
    class Meta():
        model = Pengunjung
        fields = ('nama','angkatan','keterangan')

        labels = {
            'nama': 'Nama',
            'angkatan': 'Angkatan',
            'keterangan': 'Keterangan',
        }

        widgets = {
            'nama': forms.TextInput(attrs={'class':'form-control',
                                            'placeholder':'Masukan nama anda'}),
            'angkatan': forms.Select(choices=year_choices(), attrs={'class':'form-control'}),
            'keterangan': forms.Textarea(attrs={'class':'form-control form-control-sm',
                                                'placeholder':'Masukan keterangan atau alasan'}),
        }
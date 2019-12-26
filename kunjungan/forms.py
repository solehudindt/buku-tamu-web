from django import forms
from .models import Pengunjung

class FormPengunjung(forms.ModelForm):
    class Meta():
        model = Pengunjung
        fields = (
            'nama',
            'angkatan',
            'keterangan',
        )
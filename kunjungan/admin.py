from django.contrib import admin
from .models import Pengunjung

def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    from django.http import HttpResponse
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=laporan_bukutamu.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Nama"),
        smart_str(u"Angkatan"),
        smart_str(u"Keterangan"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.nama),
            smart_str(obj.angkatan),
            smart_str(obj.keterangan),
        ])
    return response
export_csv.short_description = u"Export CSV"

class ExportLog(admin.ModelAdmin):
    actions = [export_csv]

admin.site.register(Pengunjung, ExportLog)
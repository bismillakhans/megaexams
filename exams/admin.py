from django.contrib import admin
from .models import Ques
import csv
from django.http import HttpResponse
# Register your models here.
@admin.register(Ques)
class PostAdmin(admin.ModelAdmin):
    fields = ('title','ocrtext','text','img','status','corrected','verify')
    actions= ['csv_download']
    def ocr_generate(self, request, queryset):
        data = Ques.objects.all().values_list()
        for s in data:
            s = list(s)
            writer.writerow(s)
        f.close()
        f = open('stud.csv', 'r')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=Data.csv'
        return response
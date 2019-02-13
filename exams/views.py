from django.shortcuts import render,redirect
from django.views.generic.edit import UpdateView
from .models import Ques
from django.views.generic import ListView
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter


# Create your views here.
def index(request):
    template = "exams/index.html"
    return render(request,template)

class deoList(ListView):
    model = Ques
    template_name='exams/deoList.html'
    context_object_name = 'ques'
    queryset = Ques.objects.filter(status=True)
    ordering=['-post_date']

class qcList(ListView):
    model = Ques
    template_name='exams/qcList.html'
    context_object_name = 'ques'
    queryset = Ques.objects.filter(status=True)
    ordering=['-post_date']

class deoUpdate(UpdateView):
    model = Ques
    fields = ['text',]
    queryset = Ques.objects.filter(status=True)
    template_name= 'exams/update_form.html'

def approve_group(request, pk):
    ques = Ques.objects.get(pk=pk)
    ques.status = False
    ques.save()
    return redirect(request, 'update')

def reject_group(request, pk):
    ques = Ques.objects.get(pk=pk)
    ques.status = False
    ques.save()
    return redirect(request, 'update')



    
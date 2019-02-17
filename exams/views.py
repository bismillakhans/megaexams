from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Ques
from django.contrib import messages
from django.views.generic import ListView



# Create your views here.
def index(request):
    template = "exams/index.html"
    return render(request,template)

class deoList(ListView):
    model = Ques
    template_name='exams/deoList.html'
    context_object_name = 'ques'
    queryset = Ques.objects.filter(status=True,corrected=False)
    ordering=['-post_date']

class qcList(ListView):
    model = Ques
    template_name='exams/qcList.html'
    queryset = Ques.objects.filter(status=True,corrected=True)
    context_object_name = 'ques'
    ordering=['post_date']

class deoUpdate(UpdateView):
    model = Ques
    fields = ['text','corrected']
    success_url = '/deo'
    queryset = Ques.objects.filter(status=True)
    template_name= 'exams/update_form.html'

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.corrected:
            self.object.corrected=True
        return super(deoUpdate, self).update(request, *args, **kwargs)

"""class qcUpdate(UpdateView):
    model = Ques
    fields = ['verify',]
    queryset = Ques.objects.filter(status=True)
    success_url = '/qc'
    template_name= 'exams/qc_update_form.html'"""
    
def approve_group(request, pk):
    group = Ques.objects.get(pk=pk)
    group.verify = True
    group.corrected=True
    group.save()
    return redirect('/qc')

def deny_group(request, pk):
    dele = Ques.objects.get(pk=pk)
    dele.corrected = False
    dele.verify=False
    dele.save()
    return redirect('/qc')

    """class QuesDeleteView(DeleteView):
    model = Ques
    success_url = '/qc'
    success_message = "'%(name)s'  deleted..."

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = self.object.title
        request.session['name'] = name
        message = 'Entry: ' + request.session['name'] + ' deleted successfully'
        messages.success(self.request, message)
        return super(QuesDeleteView, self).delete(request, *args, **kwargs)
    """



    



    
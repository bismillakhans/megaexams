"""mega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'exams'


urlpatterns = [
path('index/', views.index, name='index'),
path('deo/', views.deoList.as_view(), name='deo'),
path('deo/<int:pk>', views.deoUpdate.as_view(), name='update'),
#path('qc/<int:pk>', views.qcUpdate.as_view(), name='qc_update'),
path('qc/', views.qcList.as_view(), name='qc'),
#url(r'^qc/(?P<pk>\d+)/$', views.QuesDeleteView.as_view(), name='qcdelete'),
url(r'^qc(?P<pk>\d+)/$', views.deny_group, name ='reject'),
url(r'^qc(?P<pk>\d+)/$', views.approve_group, name ='verify'),
]

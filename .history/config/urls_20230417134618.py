
from django.contrib import admin
from django.urls import path

from django.shortcuts import render
from django.http import HttpResponse

def iletisim(request):
    return HttpResponse('<h1>Hi</h1>')

urlpatterns = [
    path('admin/', admin.site.urls),
]

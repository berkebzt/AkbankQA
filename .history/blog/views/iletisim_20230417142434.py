from django.shortcuts import render
from django.http import HttpResponse

def iletisim(request):
    context = {
        'name': 'Berke Deniz'
    }
    return render(request, 'pages/anasayfa.html',context=context)
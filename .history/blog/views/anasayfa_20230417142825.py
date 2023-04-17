from django.urls import path, include
from blog.views import iletisim

def mainpage(request):
    context = {
        'name': 'Berke Deniz'
    }
    return render(request, 'pages/anasayfa.html',context=context)
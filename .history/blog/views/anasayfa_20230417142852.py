from django.shortcuts import render

def mainpage(request):
    context = {
        'name': 'Berke Deniz'
    }
    return render(request, 'pages/anasayfa.html',context=context)
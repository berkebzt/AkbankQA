
from django.urls import path , include
from blog.views import iletisim, mainpage 



urlpatterns = [
    path('',mainpage, name = 'mainpage'),
    path('iletisim', iletisim, name = 'iletisim'),
    
]
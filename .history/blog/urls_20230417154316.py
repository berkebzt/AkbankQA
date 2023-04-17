
from django.urls import path , include
from blog.views import iletisim, mainpage 



urlpatterns = [
    path('',mainpage),
    path('iletisim', iletisim),
    
]

from django.urls import path , include
from blog.views import iletisim



urlpatterns = [
    path('',anasayfa),
    path('iletisim', iletisim),
    
]
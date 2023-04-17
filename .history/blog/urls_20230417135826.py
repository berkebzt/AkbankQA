from django.contrib import admin
from django.urls import path , include
from blog.views import iletisim



urlpatterns = [
    path('admin/', admin.site.urls),
    path('iletisim', iletisim),
    
]

from django.contrib import admin
from django.urls import path , include
from blog.views import iletisim
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    
]

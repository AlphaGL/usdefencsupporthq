from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, 'usdefencsupport/404.html', status=404)

handler404 = 'usdefencsupporthq.urls.custom_404'  # This is correct!

urlpatterns = [
    path('wp_admin/', admin.site.urls),
    path('', include('usdefencsupport.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

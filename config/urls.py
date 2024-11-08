# config/urls.py

# Modul Django
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# my module
from app.main import views


urlpatterns = [
    # main
    path('halodunia/', views.halodunia),
    # admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from driveNation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home),
    path('vehicle', views.vehicle),
    path('register', views.register),
    path('login', views.login)
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
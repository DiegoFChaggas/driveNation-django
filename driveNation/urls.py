from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from driveNation import views

urlpatterns = [
    path('', views.home, name="home"),
    path('vehicles', views.vehicle, name="vehicles"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('vehicles/rental/<int:id>/', views.rental, name="rental")
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
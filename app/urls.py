
from django.contrib import admin
from django.urls import path, include
from forecast.views import weather, ola

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/', weather, name='weather'),
]

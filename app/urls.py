
from django.contrib import admin
from django.urls import path
from forecast.views import weather

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/', weather, name='weather'),
]

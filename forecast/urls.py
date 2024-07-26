from django.urls import path
from forecast.views import ola

urlspatterns = [
    path("", ola,name='ola'),
]
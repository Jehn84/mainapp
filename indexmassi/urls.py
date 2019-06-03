from django.urls import path
from . import views


urlpatterns = [
    path('', views.indexmassi, name='indexmassi'),
]

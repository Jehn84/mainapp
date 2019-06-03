from django.urls import path
from . import views


urlpatterns = [
    path('', views.weight_index, name='weight_index'),
]

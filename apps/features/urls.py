from django.urls import path
from . import views

app_name = 'features'

urlpatterns = [
    path('', views.features, name='features'),
]
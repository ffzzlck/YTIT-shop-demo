from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='home'),
    path('product/', views.product_view, name='product'),
    path('product_single/', views.product_single, name='product-single'),
    path('view-up/<int:pk>/', views.views_up, name='views_up'),
    path('product-detail/<int:pk>/', views.product_detail, name='detail'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
   # path('', views.product, name='product'),
    path('product', views.product, name='product'),

]

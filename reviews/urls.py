from django.urls import path
from . import views


path('<int:product_id>/add_review', views.add_review, name='add_review'),

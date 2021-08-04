from django.urls import path
from wishlists import views

urlpatterns = [
    path('', views.view_wishlist, name='view_wishlist'),
]

from django.urls import path
from wishlists import views

urlpatterns = [
    path('', views.view_wishlist, name='view_wishlist'),
    path('add_to_wishlist/<product_id>/',
         views.add_to_wishlist, name='add_to_wishlist'),
    #path('delete/<int:review_id>/<int:product_id>/', views.delete_product_wishlist, name='delete_product_wishlist'),
]

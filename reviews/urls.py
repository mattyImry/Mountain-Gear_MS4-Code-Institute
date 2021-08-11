from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/', views.add_review, name='add_review'),
    path('edit/<int:review_id>/<int:product_id>', views.edit_review,
         name='edit_review'),
    path('delete/<int:wishlistitem_id>/<int:product_id>', views.delete_review,
         name='delete_review'),
]

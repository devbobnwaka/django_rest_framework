from django.urls import path

from . import views

urlpatterns = [
    # path('<int:pk>', views.ProductDetailAPIView.as_view()) #this or the one below works
    # path('', views.product_create_view),
    path('', views.product_list_create_view, name='product-list'),
    path('<int:pk>/update/', views.product_update_view, name='product-edit'), 
    path('<int:pk>/delete/', views.product_destroy_view),
    path('<int:pk>/', views.product_detail_view, name='product-detail'),
]

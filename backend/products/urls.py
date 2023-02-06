from django.urls import path

from . import views

urlpatterns = [
    # path('<int:pk>', views.ProductDetailAPIView.as_view()) #this or the one below works
    # path('', views.product_create_view),
    path('', views.product_list_create_view),
    # path('<int:pk>/', views.product_detail_view),
]

from django.urls import path

from . import views

urlpatterns = [
    # path('<int:pk>', views.ProductDetailAPIView.as_view()) #this or the one below works
    path('<int:pk>/', views.product_detail_view)
]

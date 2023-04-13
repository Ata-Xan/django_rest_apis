from django.urls import path

from . import views

urlpatterns = [
    # another way of writing the path to view is to have 
    # an instance of the class in the view and put the varialbe
    # here: views.product_detail_view
    # path('', views.product_mixin_view),
    # path('<int:pk>/', views.product_mixin_view),
    path('', views.product_list_create_view, name='product-list'),
    path('<int:pk>/update/', views.product_update_view, name="product-edit" ),
    path('<int:pk>/delete/', views.product_destroy_view),
    path('<int:pk>/', views.product_detail_view, name='product-detail'),
    
]
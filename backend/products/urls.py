from django.urls import path

from . import views

urlpatterns = [
    # another way of writing the path to view is to have 
    # an instance of the class in the view and put the varialbe
    # here: views.product_detail_view
    path('<int:pk>/', views.product_detail_view)
]
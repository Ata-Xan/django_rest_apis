from django.shortcuts import render
from rest_framework import generics

from .models import Product
from .serializers import PrdocutSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = PrdocutSerializer

# Create your views here.

product_detail_view = ProductDetailAPIView.as_view()
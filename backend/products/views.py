from django.shortcuts import render
from rest_framework import generics
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import get_object_or_404
from .serializers import PrdocutSerializer
# if the request is sent by post method then it would be a crete operation otherwise (get) it would be a list 
# view.
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = PrdocutSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # return super().perform_create(serializer)
        # print(serializer)
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_date.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
        #send a django signal



product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = PrdocutSerializer

# Create your views here.

product_detail_view = ProductDetailAPIView.as_view()



# Create your views here.



class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = PrdocutSerializer
    lookup_field='pk'
    def perform_update(self, serializer):
        instance = serializer.save()
    #   content = serializer.validated_date.get('content') or None
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = PrdocutSerializer
    lookup_field='pk'
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
# Create your views here.

product_destroy_view = ProductDestroyAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = PrdocutSerializer

# Create your views here.

product_list_view = ProductDetailAPIView.as_view()
# Althoug it workd, its better not to use this since it makes things so complicated, all the things above
# would be better.
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method =='GET':
        if pk is not None:
            obj= get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False)
            return Response(data)
        queryset= Product.objects.all()
        data = PrdocutSerializer(queryset, many=True).data
        return Response(data)
    
    if method =='POST':
        serializer = PrdocutSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content = content)
            return Response(serializer.data)
        return Response({"invalid":"not good data"}, status=400)
    

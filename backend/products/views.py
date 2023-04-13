from django.shortcuts import render
# I can remove authentication and permissions from following imports since 
# we have added these authentiation and permissions using mixins
from rest_framework import authentication, generics, mixins, permissions

from api.mixins import StaffEditorPermissionMixin
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import get_object_or_404
from .serializers import PrdocutSerializer
from api.permissions import IsStaffEditorPermission
# I can remove TokenAuthentication and IsStaffEditorPermission from following imports since 
# we have added these authentiation and permissions using mixins
from api.authentication import TokenAuthentication
from api.permissions import IsStaffEditorPermission
# if the request is sent by post method then it would be a crete operation otherwise (get) it would be a list 
# view.

class ProductMixinView(
    StaffEditorPermissionMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin, 
    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = PrdocutSerializer
    lookup_field='pk'
    def get(self, request, *args, **kwargs):#HTTP-> get
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    # def post(): #HTTP -> post

product_mixin_view = ProductMixinView.as_view()


class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = PrdocutSerializer
    # Ido not need the following authentication_classes anymore since in the setting.py for the api I've set the 
    # default authentication_classes
    # authentication_classes = [authentication.SessionAuthentication,
    #                         #   authentication.TokenAuthentication] this line is for Token but now it rewritten 
    #                         # with Bearer Authentication which is located in api/authentication.py
    # TokenAuthentication]
    # I put permissions.IsAdminUser and comment out the has_permission() function in the permissions.py and this still
    # working.:))
    # in here the permissions we want to match first should come first.(it first check if there is admin user then 
    # staffEditor user)
    # permission_classes = [permissions.IsAdminUser ,IsStaffEditorPermission]

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


class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    #  since I have used mixins and added to the inherited classes I could remove the following line
    # permission_classes = [permissions.IsAdminUser ,IsStaffEditorPermission]
    serializer_class = PrdocutSerializer

# Create your views here.

product_detail_view = ProductDetailAPIView.as_view()



# Create your views here.



class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = PrdocutSerializer
    # this way of defining authentication_classes is not acceptable, it is a better idea to have this variable
    # defined just for one view so we need to define our custom permissions to handle this kinds of situation.
    # authentication_classes = [authentication.SessionAuthentication]
    #  since I have used mixins and added to the inherited classes I could remove the following line
    # permission_classes = [permissions.IsAdminUser ,IsStaffEditorPermission]
    lookup_field='pk'
    def perform_update(self, serializer):
        instance = serializer.save()
    #   content = serializer.validated_date.get('content') or None
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = PrdocutSerializer
    #  since I have used mixins and added to the inherited classes I could remove the following line
    # permission_classes = [permissions.IsAdminUser ,IsStaffEditorPermission]
    lookup_field='pk'
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
# Create your views here.

product_destroy_view = ProductDestroyAPIView.as_view()

class ProductListAPIView(
    StaffEditorPermissionMixin,
    generics.ListAPIView):
    queryset = Product.objects.all()
    #  since I have used mixins and added to the inherited classes I could remove the following line
    # permission_classes = [permissions.IsAdminUser ,IsStaffEditorPermission]
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
    

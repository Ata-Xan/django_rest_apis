from django.shortcuts import render
import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from products.models import Product
from rest_framework.decorators import api_view
from products.serializers import PrdocutSerializer
# indicate which method for our request is allowed 
@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    data = request.data
    serializer = PrdocutSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # print(serializer.data)
        # saving data
        # instance = serializer.save()
        print(serializer.data)
        # data.save()
        return Response(serializer.data)
    else:
        return Response({"invalid":"not good data"}, status=400)

    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
        # using model_to_dict we can do the following:
        # instead of the one by one:
        # data = model_to_dict(model_data, fields=['id', 'title'])
        # if instance:
            # data = PrdocutSerializer(instance).data
        # data['title'] = model_data.title
        # data['content']=model_data.content
        # data['price'] = model_data.price
        # data['id']=model_data.id
    # return Response(data)

# Create your views here.

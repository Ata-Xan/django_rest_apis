from rest_framework import viewsets

from .models import Product
from .serializers import PrdocutSerializer


class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> Queryset
    get -> retrieve -> Product Instance Detail View
    post -> create -> New Instance
    put -> Update
    patch -> Partial Update
    delete -> destroy
    '''
    queryset = Product.objects.all()
    serializer_class = PrdocutSerializer
    lookup_field = 'pk' #default



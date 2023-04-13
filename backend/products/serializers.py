from rest_framework import serializers
from rest_framework.reverse  import reverse
from .validators import validate_title
from .models import Product

class PrdocutSerializer(serializers.ModelSerializer):
    #  how to replaced get_discount with other name in here discount after doing this we need to have another
    # function named get_discount as well to make it work.
    my_discount = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    # another way to define url
    url = serializers.HyperlinkedIdentityField( view_name='product-detail',
        lookup_field = 'pk'
    )
    edit_url = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(write_only=True)

    title = serializers.CharField(validators = [validate_title])

    class Meta:
        model=Product
        fields = [
            'url',
            'email',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    # Custom serialization validation
    # the name for this function should be like (validate_<field_name>)
    
    # we can even put his validator in another separate file.
    def validate_title(self, value):
        print('validate_title function')
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name")
        return value
    
    def get_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request') #self.request
        if request is None:
            return None
        return reverse("product-detail",kwargs={"pk":obj.pk},request = request)
    
    def get_edit_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request') #self.request
        if request is None:
            return None
        return reverse("product-edit",kwargs={"pk":obj.pk},request = request)
    
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        # try:
        return obj.get_discount()
        # except:
        #     return 'None'


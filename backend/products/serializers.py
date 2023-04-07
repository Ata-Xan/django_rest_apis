from rest_framework import serializers


from .models import Product

class PrdocutSerializer(serializers.ModelSerializer):
    #  how to replaced get_discount with other name in here discount after doing this we need to have another
    # function named get_discount as well to make it work.
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        # try:
        return obj.get_discount()
        # except:
        #     return 'None'


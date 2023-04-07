from django import forms


from .models import Product

class PrdocutForm(forms.ModelForm):
    class Meta:
        model=Product
        fields = [
            'title',
            'content',
            'price'
        ]
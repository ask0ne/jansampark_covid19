from django import forms
from retailers.models import Retailer

class RetailerForm(forms.ModelForm):
    """form for the retailers"""
    class Meta:
        model = Retailer
        fields = ['company_name', 'product', 'quantity']
        labels = {'company_name': 'Organization name', 'product': 'Product', 'quantity': 'Quantity'}
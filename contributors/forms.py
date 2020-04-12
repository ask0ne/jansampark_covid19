from django import forms
from .models import Retailer

class RetailerForm(forms.ModelForm):
    """form for the retailers"""
    class Meta:
        model = Retailer
        fields = ['company_name', 'product', 'quantity']
        labels = {'company_name': 'company', 'product': 'product', 'quantity': 'quantity'}
from rest_framework import serializers

from .models import Retailer

class RetailerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Retailer
        fields = ('company_name', 'product', 'quantity', 'lat', 'long', 'updated_on')

from django.db.models import Count, Sum
from rest_framework import viewsets


from .serializers import RetailerSerializer
from .models import Retailer

# Create your views here.

class RetailerViewSet(viewsets.ModelViewSet):
    queryset = Retailer.objects.values('company_name', 'product', 'lat', 'long').annotate(quantity=Sum('quantity'))
    # all().order_by('company_name')
    serializer_class = RetailerSerializer




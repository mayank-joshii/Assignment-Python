from django.shortcuts import render
from home.serializers import ItemSerializer
from home.models import Records
from rest_framework import viewsets, generics

# Create your views here.

class ItemListCreateView(generics.ListCreateAPIView):

    queryset = Records.objects.all()
    serializer_class = ItemSerializer

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Records.objects.all()
    serializer_class = ItemSerializer

class ItemSearchView(generics.ListAPIView):

    serializer_class = ItemSerializer

    def get_queryset(self):

        queryset = Records.objects.all()

        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        quantity = self.request.query_params.get('quantity', None)

        if name:
            queryset = queryset.filter(name__icontains=name)
        if description:        
            queryset = queryset.filter(description__icontains=description)
        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)
        if quantity is not None:    
            queryset = queryset.filter(quantity__icontains=quantity)

        
        return queryset


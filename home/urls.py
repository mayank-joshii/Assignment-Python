from django.contrib import admin
from django.urls import path, include
from home.views import ItemListCreateView, ItemDetailView, ItemSearchView
urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('details/<int:pk>', ItemDetailView.as_view(), name='item-detail'),
    path('search/', ItemSearchView.as_view(), name='item-search')
]

from django.shortcuts import render
from rest_framework import viewsets

from backend.models import Invoice, Address, InvoicePosition
from backend.serializers import InvoiceSerializer, AddressSerializer, InvoicePositionSerializer


class AddressListView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class InvoiceListView(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoicePositionListView(viewsets.ModelViewSet):
    queryset = InvoicePosition.objects.all()
    serializer_class = InvoicePositionSerializer

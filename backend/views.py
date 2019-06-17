from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from backend.models import Invoice, Address, InvoicePosition
from backend.serializers import InvoiceSerializer, AddressSerializer, InvoicePositionSerializer


class AddressListView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class InvoiceListView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoicePositionListView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = InvoicePosition.objects.all()
    serializer_class = InvoicePositionSerializer

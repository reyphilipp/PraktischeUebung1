from django.urls import path, include
from rest_framework import routers

from backend.views import InvoiceListView, AddressListView, InvoicePositionListView

router = routers.DefaultRouter()

router.register('addresses', AddressListView, base_name='address')
router.register('invoices', InvoiceListView, base_name='invoice')
router.register('invoicePositions', InvoicePositionListView, base_name='invoicePosition')

urlpatterns = [
    path('', include(router.urls))
]
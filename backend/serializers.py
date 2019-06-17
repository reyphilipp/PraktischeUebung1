from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from backend.models import Invoice, Address, InvoicePosition



class InvoicePositionSerializer(ModelSerializer):

    total_position = serializers.SerializerMethodField()


    class Meta:
        model = InvoicePosition
        fields = ('title', 'order_id', 'price', 'quantity', 'total_position')

    def get_total_position(self, obj):
        return obj.price * obj.quantity


class InvoiceSerializer(ModelSerializer):
    positions = InvoicePositionSerializer(many=True, read_only=True)
   # addresses = AddressSerializer(many=True, read_only=True)
    class Meta:
        model = Invoice
        fields = ('invoice_nr', 'invoice_date', 'positions', 'description')


class AddressSerializer(ModelSerializer):
    invoices = InvoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Address
        fields = ('name', 'zip', 'id', 'invoices')



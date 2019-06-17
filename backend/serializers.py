from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from backend.models import Invoice, Address, InvoicePosition

# murks wegen der verflixten forwärtsdeklaration
class AddressSerializerConcept(ModelSerializer):

    class Meta:
        model = Address
        fields = ('name', 'zip', 'id')


class InvoicePositionSerializer(ModelSerializer):
    total_position = serializers.SerializerMethodField()

    class Meta:
        model = InvoicePosition
        fields = ('title', 'order_id', 'price', 'quantity', 'total_position')

    def get_total_position(self, obj):
        return obj.price * obj.quantity


class InvoiceSerializer(ModelSerializer):
    address = AddressSerializerConcept(many=False, read_only=True)
    positions = InvoicePositionSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = ('address','invoice_nr', 'invoice_date', 'positions', 'description')


class AddressSerializer(AddressSerializerConcept):
    invoices = InvoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Address
        fields = ('name', 'zip', 'id', 'invoices')



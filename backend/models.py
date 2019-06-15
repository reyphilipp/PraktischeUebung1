from django.db import models

class Address(models.Model):
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=120)
    street = models.CharField(max_length=120)
    house_nr = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

class Invoice(models.Model):
    description = models.CharField(max_length=120)
    invoice_nr = models.CharField(max_length=60)
    invoice_date = models.DateField()

    address = models.ForeignKey('Address', related_name='addresses', on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'Invoice: %s' % self.invoice_nr

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

class InvoicePosition(models.Model):
    order_id = models.IntegerField()
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity =models.IntegerField()

    invoice = models.ForeignKey('Invoice', related_name='positions', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.order_id, self.title)

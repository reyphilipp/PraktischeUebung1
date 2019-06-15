from django.contrib import admin

from backend.models import *

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    pass

@admin.register(InvoicePosition)
class InvoicePositionAdmin(admin.ModelAdmin):
    pass

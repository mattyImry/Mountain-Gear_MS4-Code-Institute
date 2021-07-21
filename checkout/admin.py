from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    add and edit order line
    items from admin
    Code taken from Boutique Ado
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):

    """
    Creates fields for the order
    Code taken from Boutique Ado
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'user_profile', 'date',
                       'delivery_cost', 'order_total',
                       'sum_total', 'original_cart',
                       'stripe_pid')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'sum_total', 'original_cart',
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'sum_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)

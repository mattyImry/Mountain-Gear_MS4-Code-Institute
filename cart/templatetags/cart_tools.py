from django import template

"""
Code taken from Boutique Ado CI tutorial
"""
register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity

from distutils.sysconfig import customize_compiler
import site
from django.contrib import admin
from .models import *

admin.site.register(customer)
admin.site.register(delivery_address)
admin.site.register(payment_method)
admin.site.register(customer_order)
admin.site.register(product)
admin.site.register(order_item)
admin.site.register(review)
admin.site.register(book)
admin.site.register(filter_tag)
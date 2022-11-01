from distutils.sysconfig import customize_compiler
import site
from django.contrib import admin
from .models import *

admin.site.register(customer_order)
admin.site.register(product)
admin.site.register(order_item)
admin.site.register(book)
admin.site.register(filter_tag)
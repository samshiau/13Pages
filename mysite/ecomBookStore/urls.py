from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
                  path('', views.index, name='index'),
                  path('register', views.register, name='register'),
                  path('login', views.login, name='login'),
                  path('cart', views.cart, name='cart'),
                  path('admin', admin.site.urls),
                  path('add-to-cart', views.add_to_cart, name="add-to-cart"),
                  path('delete-from-cart', views.delete_cart_item, name="delete-from-cart'"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # image config

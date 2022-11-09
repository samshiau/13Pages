from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('cart', views.cart, name='cart'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # image config
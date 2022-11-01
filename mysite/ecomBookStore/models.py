from email.policy import default
from enum import unique
from operator import mod
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

#extra functions
class RangeIntegerField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        validators = kwargs.pop("validators", [])
        
        # turn min_value and max_value params into validators
        min_value = kwargs.pop("min_value", None)
        if min_value is not None:
            validators.append(MinValueValidator(min_value))
        max_value = kwargs.pop("max_value", None)
        if max_value is not None:
            validators.append(MaxValueValidator(max_value))

        kwargs["validators"] = validators

        super().__init__(*args, **kwargs)

class RangeBigIntegerField(models.BigIntegerField):
    def __init__(self, *args, **kwargs):
        validators = kwargs.pop("validators", [])
        
        # turn min_value and max_value params into validators
        min_value = kwargs.pop("min_value", None)
        if min_value is not None:
            validators.append(MinValueValidator(min_value))
        max_value = kwargs.pop("max_value", None)
        if max_value is not None:
            validators.append(MaxValueValidator(max_value))

        kwargs["validators"] = validators

        super().__init__(*args, **kwargs)

# Create your models here.
class customer_order(models.Model):
    orderID = models.AutoField(primary_key=True)
    customerID = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.BooleanField(default=True)

    def __str__(self):
        return str(self.orderID)
    
class product(models.Model):
    productID = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=20)
    productDesc = models.CharField(max_length=300)
    productPrice = models.DecimalField(max_digits=5, decimal_places=2)
    currentStock = models.PositiveIntegerField()
    products = models.ManyToManyField(customer_order, through='order_item')

    def __str__(self):
        return self.productName

class order_item(models.Model):
    orderID = models.ForeignKey(customer_order, on_delete=models.CASCADE)
    productID = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.orderID) + " " + str(self.productID)

class book(models.Model):
    productID = models.OneToOneField(product, on_delete=models.CASCADE, primary_key=True)
    ISBN = models.CharField(max_length=13, unique=True)
    Author = models.CharField(max_length=40)
    publisher = models.CharField(max_length=40)

    def __str__(self):
        return self.productID.productName

class filter_tag(models.Model):
    # NOTE: the type will use following format (without number space and dash, case sensitive):
    # 1 - Office Supplies
    # 2 - Food and Drinks
    # 3 - Toys
    # 4 - Fantasy
    # 5 - Music
    # 6 - Movies
    # 7 - Books
    # 8 - Comic
    # 9 - Manga
    # 10 - Horror
    # 11 - Thriller
    # 12 - Romance
    # 13 - Adventure
    # 14 - Textbook
    # 15 - For Kids
    # 16 - Digital
    # 17 - Paperback
    # 18 - Hardcover
    # 19 - Science
    # 20 - Mystery
    # 21 - Humor
    tagID = models.AutoField(primary_key=True)
    tagName = models.CharField(max_length=20)
    products = models.ManyToManyField(product)

    def __str__(self):
        return self.tagName
from operator import mod
from django.db import models

# Create your models here.
class Item(models.Model): 
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)

    # NOTE: the type will use following format (without number space and dash, case sensitive):
    #  1 - book
    #  2 - officeSupply
    #  3 - snack
    #  4 - gift
    #  5 - idea
    #  6 - movie
    #  7 - music
    #  8 - toy
    #  9 - other
    item_type = models.CharField(max_length=100)
    item_price = models.IntegerField()
    item_quantity = models.IntegerField()
    item_description = models.CharField(max_length=500)

    def __str__(self):
        return self.item_name

class Book(models.Model):
    book_id = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True)
    book_author = models.CharField(max_length=100)
    book_isbn = models.CharField(max_length=100)

    def __str__(self):
        return self.book_id.item_name
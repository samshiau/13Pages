from django.db import models

# Create your models here.
class Item(models.Model): 
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=100)
    item_price = models.IntegerField()
    item_quantity = models.IntegerField()
from django.db import models
from cloudinary.models import CloudinaryField
from hivetechbackend.constants import PRODUCT_TYPE

# Create your models here.

class Product(models.Model):
    class Meta(object):
        db_table = 'product'

    name= models.CharField(
        "Name", blank=False, null=False, max_length=50
    )
    description= models.CharField(
        "Description", blank=True, null=True, max_length=300
    )
    price= models.FloatField(
        "Price", blank=False, null=False, default=100 
    )
    image= CloudinaryField(
        "Product Image", blank=True, null=True
    )
    type= models.CharField(
        "Type", blank=False, null=False, max_length=50, choices=PRODUCT_TYPE
    )

    #We need to chnge the catagory after creating catagories app
    category= models.CharField(
        'Category', blank=True, null=True,max_length=300
    )
    def __str__(self):
        return self.name


from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    class Meta(object):
        db_table='category'
    name=models.CharField(
        'Name', blank=False, null=False, max_length=50, db_index=True
    )
    image= CloudinaryField(
        'Image', blank=True, null=True
    )
    created_at=models.DateTimeField(
        'created time', blank=True, auto_now_add=True
    )
    updated_at=models.DateTimeField(
        'updated time', blank=True, auto_now=True
    )

    def __str__(self):
        return self.name


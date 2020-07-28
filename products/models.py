from django.db import models
from datetime import datetime
# Create your models here.

class Category(models.Model):
    cate_name = models.CharField(max_length=100)
    cate_image = models.ImageField(upload_to='product_images/',null=True)

class Products(models.Model):
    c_id = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    cate_name = models.CharField(max_length=100,null=True)
    pro_name = models.CharField(max_length=100)
    pro_image = models.ImageField(upload_to='SubProduct_images/',null=True)
    product_price = models.IntegerField()
    produ_features = models.CharField(max_length=500,null=True)
    prod_description = models.CharField(max_length=500)
    product_create_date = models.DateTimeField(default=datetime.now, blank=True)


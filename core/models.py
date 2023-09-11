from distutils.command.upload import upload
from pyexpat import model
from tokenize import blank_re
from django.db import models
from datetime import datetime
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    desription=models.TextField()
    price=models.DecimalField(max_digits=8,decimal_places=0)
    image=models.ImageField(upload_to="photos/%Y/%m/%d/",default="default.jpg",null=True,blank=True)
    is_active=models.BooleanField(default=True)
    publish_date=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    phone=models.CharField(max_length=10)
    adrees=models.CharField(max_length=100)
    city=models.CharField(max_length=20)
    total=models.DecimalField(max_digits=6,decimal_places=1,null=True)
     

    def __str__(self):
        return str(self.product)

class Pages(models.Model):
    about_us=models.TextField()
    shipping=models.TextField()
    privacyPolicy=models.TextField()

    def __str__(self):
        return "pages"

    class Meta:
        verbose_name_plural="Pages"


class MaintenceMode(models.Model):
    maintence=models.BooleanField(default=False)


    def save(self,*args,**kwargs):
        if self.__class__.objects.count():
            self.pk=self.__class__.objects.first().pk
        super().save(*args,**kwargs)


    def __str__(self):
        return "Maintence Mode"
class ProductImages(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    pics=models.ImageField(upload_to="photos/pics",null=True)
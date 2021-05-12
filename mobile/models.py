from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=150)
    price=models.FloatField()
    specifications=models.CharField(max_length=150)
    image=models.ImageField(upload_to="ïmages/")

    def __str__(self):
        return self.product_name

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)#Product is the above model name
    address=models.CharField(max_length=200)
    choices=(
        ("ordered","ordered"),
        ("delivered","delivered"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=100,choices=choices,default="ordered")
    user=models.CharField(max_length=200)


class Carts(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)
    price_total=models.PositiveBigIntegerField(editable=False,blank=True,null=True)
    user = models.CharField(max_length=120,null=True)
    def save(self,*args,**kwargs):
        self.price_total=self.product.price*self.quantity
        super(Carts, self).save(*args,**kwargs)
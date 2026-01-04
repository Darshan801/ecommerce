from django.db import models

# Create your models here.
class Contact(models.Model):
    # Contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    desc=models.TextField(max_length=100)
    phonenumber=models.IntegerField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField( max_length=100)
    category=models.CharField( max_length=50, default="")
    sub_category=models.CharField( max_length=50, default="")
    price=models.IntegerField(default=0)
    desc=models.CharField( max_length=300)

    image=models.ImageField(upload_to='images/images')

    def __str__(self):
        return self.product_name
    
    def save(self,*args, **kwargs):
        if (self.product_name , self.category,self.sub_category):
            self.product_name=self.product_name.title()
            self.category=self.category.title()
            self.sub_category=self.sub_category.title()
            super().save(*args , **kwargs)

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField( max_length=50)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address1=models.CharField(max_length=50)
    address2=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    oid=models.CharField(max_length=50,blank=True)
    amountpaid=models.CharField(max_length=50,blank=True,null=True)
    # paymentstatus=models.CharField(max_length=50,blank=True,null=)
    phone=models.CharField(max_length=50,default="")

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=50)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+"..."

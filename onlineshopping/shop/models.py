from django.db import models
from django.contrib.auth.models import User

class UserInfo(User):
    age=models.IntegerField()
    contact=models.CharField(max_length=15)
    gender=models.CharField(max_length=10)

    class Meta:
        db_table='user_info'

class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=300)

    class Meta:
        db_table='category'
    def __str__(s):
        return s.name
   

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    img=models.ImageField(upload_to='images',default='')
    description=models.CharField(max_length=500)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table='product'

    def __str__(s):
        return s.name

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table='cart'

class Order(models.Model):
    totalBill=models.IntegerField()
    orderDate=models.DateField(auto_now=True)
    status=models.CharField(max_length=50,default="Processing")
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table='myorder'


#Manager
from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	address=models.TextField()
	profile_pic=models.ImageField(upload_to="profile_pic/")
	password=models.CharField(max_length=100)
	usertype=models.CharField(max_length=100,default="user")

	def __str__(self):
		return self.fname+" - "+self.lname

class Product(models.Model):
	seller=models.ForeignKey(User,on_delete=models.CASCADE)
	product_company=models.CharField(max_length=100)
	product_model=models.CharField(max_length=100)
	product_desc=models.TextField()
	product_price=models.IntegerField()
	product_image=models.ImageField(upload_to="product_image/")

	def __str__(self):
		return self.seller.fname+" - "+self.product_company

class Wishlist(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.fname+" - "+self.product.product_company

class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)
	product_price=models.IntegerField()
	product_qty=models.IntegerField(default=1)
	total_price=models.IntegerField()
	def __str__(self):
		return self.user.fname+" - "+self.product.product_company

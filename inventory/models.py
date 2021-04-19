from django.db import models
import datetime
from decimal import *


# Create your models here.
def currencyInIndiaFormat(n):
  d =n 
  if d.as_tuple().exponent < -2:
    s = str(n)
  else:
    s = '{0:.2f}'.format(n)
  l = len(s)
  i = l-1;
  res = ''
  flag = 0
  k = 0
  while i>=0:
    if flag==0:
      res = res + s[i]
      if s[i]=='.':
        flag = 1
    elif flag==1:
      k = k + 1
      res = res + s[i]
      if k==3 and i-1>=0:
        res = res + ','
        flag = 2
        k = 0
    else:
      k = k + 1
      res = res + s[i]
      if k==2 and i-1>=0:
        res = res + ','
        flag = 2
        k = 0
    i = i - 1

  return res[::-1]


class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    email = models.EmailField()
    registered_on = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name


class Vendor(models.Model):

  name= models.CharField(max_length=50)
  address = models.CharField(max_length=100)
  mobile_no = models.CharField(max_length=10)
  email= models.EmailField()
  registered_on = models.DateTimeField(auto_now_add=True,blank=True)

  def __str__(self):
      return self.name

  


class ProductCategory(models.Model):

    category_name = models.CharField(max_length=30)
    labor_charge = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.category_name + ' , '+ str(self.labor_charge)
    
    class Meta:
        verbose_name_plural = "Product Categories"



class ProductType(models.Model):
    type = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10,decimal_places=2, null=True)



    def __str__(self):
        return self.type + ' , '+ str(self.price)
    class Meta:
        verbose_name_plural = "Product Types"


class Product(models.Model):

    title = models.CharField(max_length=30)
    category = models.ForeignKey('ProductCategory',on_delete= models.CASCADE)
    type = models.ForeignKey('ProductType',on_delete = models.CASCADE)
    weight = models.DecimalField(max_digits=10,decimal_places=3 ,default=0) #weight in gram
    jarti = models.DecimalField(max_digits=10,decimal_places=3,default=0)
    vendor = models.ForeignKey('Vendor',on_delete=models.SET_NULL,null=True)
    image = models.ImageField(null=True,default='imageplaceholder.jpg')
    added = models.DateTimeField(auto_now_add=True,blank=True)
    

    def __str__(self):
        return self.title
    
    

    def getprice(self):
        latest_price = ((self.weight + self.jarti)*self.type.price)/Decimal(11.66) + self.category.labor_charge
        # return round(latest_price,ndigits=0)
        return currencyInIndiaFormat(
            round(latest_price,ndigits=2)
            )
    
    getprice.short_description = 'Price'

    def getvendor(self):
        # vendor_get= self.purchasefromvendor_set.last()
        # vendor_name = vendor_get
        # print(vendor_name)
        # return vendor_name
        vendor = self.vendor
        return vendor
    
    getvendor.short_description = 'Vendor'

class PurchaseFromVendor(models.Model):
  order_id = models.CharField(max_length=20)
  vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True,blank=True)
  product = models.ManyToManyField(Product)
  order_date = models.DateTimeField()

  def __str__(self):
      return self.order_id + ' '+ str(self.vendor)

ORDER_STATUS_CHOICES =[

    ('pending', 'Pending'),
    ('processing', 'Processing'),
    ('canceled', 'Cancelled'),
    ('completed', 'Completed'),
    ('onhold', 'OnHold'),

]

class Order(models.Model):
  product = models.ManyToManyField(Product)
  customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
  date_ordered= models.DateTimeField(auto_now_add=True)
  order_status = models.CharField(choices=ORDER_STATUS_CHOICES,max_length=30,default='pending')
  notes = models.CharField(max_length=100)

  def __str__(self):
    return str(self.id)
  



  







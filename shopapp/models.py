from django.db import models
import datetime
import os
from django.contrib.auth.models import User 

def getfilename(request,filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s"%(now_time,filename)
    return os.path.join("uploads/",new_filename)


class catagory(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=getfilename,null=True,blank=True)
    description= models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="o-show,1-hidden")  
    created_at = models.DateTimeField(auto_now_add=True)
    
def __str__(self):
    return self.name

class product(models.Model):
    category = models.ForeignKey(catagory,on_delete=models.CASCADE ) 
    name = models.CharField(max_length=150,null=False,blank=False)
    vendor = models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to=getfilename,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=True,blank=True)
    description= models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="o-show,1-hidden")
    trending = models.BooleanField(default=False,help_text="o-default,1-Trending")
    created_at = models.DateTimeField(auto_now_add=True)

class cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
       return self.product_qty*self.product.selling_price
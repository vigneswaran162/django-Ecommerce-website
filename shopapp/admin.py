from django.contrib import admin
from  .models import *

# Register your models here.
class admin_cat(admin.ModelAdmin):
    list_display=['name']
    
class admin_prod(admin.ModelAdmin):
      list_display=['name']

admin.site.register(catagory),
admin.site.register(product)

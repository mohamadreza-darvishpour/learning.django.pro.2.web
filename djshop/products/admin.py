from django.contrib import admin

# Register your models here.
from . import models

class product_admin(admin.ModelAdmin):
#    readonly_fields= ['slug','is_active']
    prepopulated_fields = {
        'slug':['title'],
    }
    list_display = ('id','title','short_description','category','is_active','price','slug','product_infos')
    list_filter = ['is_active','price']
    list_editable = ['is_active','price',"category",'product_infos']


admin.site.register(models.products,product_admin)
admin.site.register(models.product_category)
admin.site.register(models.product_info)
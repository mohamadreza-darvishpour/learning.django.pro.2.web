from django.contrib import admin

# Register your models here.
from . import models

class product_admin(admin.ModelAdmin):
#    readonly_fields= ['slug','is_active']
    prepopulated_fields = {
        'slug':['title'],
    }
    list_display = ('id','short_description','price','slug')
    list_filter = ['price']
    list_editable = ['price',]


admin.site.register(models.products,product_admin)
admin.site.register(models.product_category)
admin.site.register(models.product_info)
admin.site.register(models.product_tag)
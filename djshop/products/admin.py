from django.contrib import admin

# Register your models here.
from . import models

class product_admin(admin.ModelAdmin):
#    readonly_fields= ['slug','is_active']
    prepopulated_fields = {
        'slug':['title'],
    }


admin.site.register(models.products,product_admin)
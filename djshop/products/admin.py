from django.contrib import admin

# Register your models here.
from . import models

class product_admin(admin.ModelAdmin):
#    readonly_fields= ['slug','is_active']
    prepopulated_fields = {
        'slug':['title'],
    }
    list_display = ('short_description','is_active','price','slug')
    list_filter = ['is_active','price']
    list_editable = ['is_active','price']


admin.site.register(models.products,product_admin)
from django.contrib import admin

# Register your models here.
from . import models

class productadmin(admin.ModelAdmin):
    list_display = ['id','title','price','slug','short_description','is_active','is_deleted']
    list_filter = ('price','is_active')
    list_editable = ['title','price','is_active' ]


admin.site.register(models.products,productadmin)
admin.site.register(models.product_category)
admin.site.register(models.product_info)
admin.site.register(models.product_tag)
admin.site.register(models.product_brand)
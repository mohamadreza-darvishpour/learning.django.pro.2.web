from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
from django.utils.text import slugify



    
#make one to one relation
class product_info(models.Model):
    color = models.CharField(max_length=300,verbose_name='prod_info_color',null=True)
    size = models.CharField(max_length=200,verbose_name ='prod_info_size',null= True)
    def __str__(self):
        return f'{self.color}_{self.size}'
    


class product_category(models.Model):
    title = models.CharField(max_length= 300,db_index=True,verbose_name ='title of subject',)
    url_title = models.CharField(max_length=300,db_index=True,verbose_name = 'title of url',)
    is_active = models.BooleanField(verbose_name="is active/not active")
    is_deleted = models.BooleanField(verbose_name="deleted/undeleted")

    def __str__(self):
        return (f'{self.title}  {self.url_title}')
    #add Meta class to change some features
    class Meta:
        verbose_name = "Meta_product_category"
        verbose_name_plural = "Meta_plural_categories"






class products(models.Model):
    title = models.CharField(max_length=30,verbose_name= 'title')
    price = models.IntegerField(verbose_name="price")
    description = models.TextField(verbose_name="main_description",db_index=True,)
    short_description = models.CharField(max_length=390,null=True,db_index=True,verbose_name ='short-description')
    is_active = models.BooleanField(default=False,verbose_name="is_active/not_active")
    slug = models.SlugField(max_length=300,editable=True,blank=True,default="",null=False,db_index=True,unique=True)
    category = models.ManyToManyField(product_category,related_name="product_category",verbose_name="categories")
    is_deleted = models.BooleanField(verbose_name="deleted/undeleted")
    
    def __str__(self):
        return f'{self.title}____{self.price}'
    
    def get_absolute_url(self):
        from django.urls import reverse
        url_to_return = f'{str(self.id)}_{self.slug}'
        return reverse("prod_detail",args=[url_to_return,] )
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)



class product_tag(models.Model):
    product = models.ForeignKey(products, on_delete=models.CASCADE,related_name="product_tags")
    caption = models.CharField(max_length=300,db_index=True,verbose_name = 'tags-and-caption')
    class Meta:
        verbose_name ="tag"
    def __str__(self):
        return self.title
    

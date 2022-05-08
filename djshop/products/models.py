from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
from django.utils.text import slugify


class product_category(models.Model):
    title = models.CharField(max_length= 300,verbose_name ='title of subject',)
    url_title = models.CharField(max_length=300,verbose_name = 'title of url',)
    def __str__(self):
        return self.title

    


class products(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    category = models.ForeignKey(product_category, on_delete=models.CASCADE,null=True) #or models.Set_Null or models.PROTECT
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(6),
        ],
        default = 0,
    )
    short_description = models.CharField(max_length=390,null=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(editable=True,blank=True,default="",null=False,db_index=True)
    def __str__(self):
        return f'{self.title}____{self.price}'
    
    def get_absolute_url(self):
        from django.urls import reverse
        url_to_return = f'{str(self.id)}_{self.slug}'
        return reverse("prod_detail",args=[url_to_return,] )
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)



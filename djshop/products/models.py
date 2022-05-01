from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
from django.utils.text import slugify


class products(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(6),
        ],
        default = 0,
    )
    short_description = models.CharField(max_length=390,null=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(default="",null=False,db_index=True)
    def __str__(self):
        return f'{self.title}____{self.price}'
    
    def get_absolute_url(self):
        from django.urls import reverse
        url_to_return = f'{str(self.id)}_{self.slug}'
        return reverse("prod_detail",args=[url_to_return,] )
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

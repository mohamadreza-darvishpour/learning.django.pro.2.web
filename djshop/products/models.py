from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.



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

    def __str__(self):
        return f'{self.title}____{self.price}'
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("prod_detail",args=[self.id,] )
    #hello from github site...

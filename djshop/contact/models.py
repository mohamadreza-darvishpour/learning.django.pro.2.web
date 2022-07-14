from django.db import models

# Create your models here.
class profile_images(models.Model):
    image = models.FileField(upload_to="uploaded_files")

class contact_us(models.Model):
    title = models.CharField(max_length=200,verbose_name="title")
    email = models.EmailField(max_length=300,verbose_name = "email" )
    full_name = models.CharField(max_length=300,verbose_name="name" )
    message = models.TextField(verbose_name= "message" )
    is_read_by_admin = models.BooleanField(verbose_name="is read by admin?",default=False)
    created_date = models.DateTimeField(verbose_name= "created_date",auto_now_add=True)
    response = models.TextField(verbose_name="response",null=True,blank=True)
   
    class Meta:

        verbose_name="contact us"
        verbose_name_plural = "list of contact us"
    def __str__(self):
        return self.title 
    
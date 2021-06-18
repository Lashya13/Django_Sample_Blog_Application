from django.db import models

# Create your models here.
class PostTable(models.Model):
   title =models.CharField(max_length=200)
   description =models.TextField()
   #blog_image = models.ImageField() 
   publisher_time = models.DateTimeField(auto_now_add=True)
  
   

   def __str__(self):
       return self.title
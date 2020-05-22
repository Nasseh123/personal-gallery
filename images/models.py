from django.db import models

# Create your models here.
class image(models.Model):
    image=models.ImageField(upload_to='articles/')
    image_name=models.CharField(max_length=30)
    image_description=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.image_name

    class Meta:
        ordering=['pub_date']   

class location(models.Model):
    location_name=models.CharField(max_length=60)

class category(models.Model):
    category_name=models.CharField(max_length=60)
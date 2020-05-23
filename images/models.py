from django.db import models
import datetime as dt 

# Create your models here.
class location(models.Model):
    location_name=models.CharField(max_length=60)
    def __str__(self):
        return self.location_name
class category(models.Model):
    category_name=models.CharField(max_length=60)

    def __str__(self):
        return self.category_name

class image(models.Model):
    image=models.ImageField(upload_to='articles/')
    image_name=models.CharField(max_length=30)
    image_description=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)
    location=models.ForeignKey(location,on_delete=models.CASCADE)
    category=models.ForeignKey(category,on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    class Meta:
        ordering=['pub_date']   




  


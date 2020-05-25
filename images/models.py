from django.db import models
import datetime as dt 

# Create your models here.
class location(models.Model):
    location_name=models.CharField(max_length=60)
    def __str__(self):
        return self.location_name
    
    def save_location(self):
        self.save()

    @classmethod
    def alllocation(cls):
        locations=cls.objects.all()
        return locations

class category(models.Model):
    category_name=models.CharField(max_length=60)
    
    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()
    
    @classmethod
    def allcategory(cls):
        categorys=cls.objects.all()
        
        return categorys

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

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    @ classmethod
    def update_image(cls,details):
        updated=image.objects.update(image=details)
        return updated
        # self.filter(id=self.id).update(image=details)

    @classmethod
    def allimages(cls):
        imaged=cls.objects.all()
        return imaged
    
    @classmethod
    def search_by_name(cls,search_name):
        imaged=cls.objects.filter(image_name__icontains=search_name)
        return imaged


  


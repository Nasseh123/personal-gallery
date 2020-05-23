from django.test import TestCase
from .models import image,location,category
import datetime as dt
# Create your tests here.
class locationTestClass(TestCase):
    def setUp(self):
        self.location=location(location_name='nairobi')
    def test_instance(self):
        self.assertTrue(isinstance(self.location,location))
    



class imageTestClass(TestCase):
    def setUp(self):
        self.location=location(id=2)
        self.category=category(id=1,category_name='Beauty')
        self.image=image(id=1,image='articles/smiley-4832482_1920.png',image_name='smiley-4832482_1920.png',image_description="Good picture",
                        pub_date='2020-05-19 12:20:58.843802+03',location_id=2,category_id=1)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.image,image))

    def test_save_method(self):
        self.location.save_location()
        self.category.save_category()
        self.image.save_image()
        imaged=image.objects.all()
        self.assertTrue(len(imaged)==1)

    def test_delete_image(self):
        self.location.save_location()
        self.category.save_category()
        self.image.save_image()
        self.image.delete_image()
        imaged=image.objects.all()
        self.assertTrue(len(imaged)==0)

    def test_update_image(self):
        self.location.save_location()
        self.category.save_category()
        self.image.save_image()
        # self.image.update_image('articles/jokes-4832482_1920.png')
        imaged=image.objects.update(image='articles/jokes-4832482_1920.png')
        
        print(imaged)
        self.assertTrue(imaged,self.image.image)

    # def test_get_image_by_id(self):
    #     self.location.save_location()
    #     self.category.save_category()
    #     self.
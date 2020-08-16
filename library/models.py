from django.db import models
from tinymce import HTMLField
# Create your models here.


class E_Resources(models.Model):
    title = models.CharField(max_length=254)
    link = models.CharField(max_length=254)


class library_page(models.Model):
    title = models.CharField( max_length=250)
    page_content = HTMLField()
    contact_info = HTMLField()

    def __str__(self):
        return self.title
    

class thesis_title(models.Model):
    name = models.CharField( max_length=250)
    file = models.FileField( upload_to="thesis/", max_length=254)


class page_image(models.Model):
    library = models.ForeignKey(library_page, on_delete=models.CASCADE)    
    image = models.ImageField(upload_to="library_images/", height_field=None, width_field=None, max_length=None)
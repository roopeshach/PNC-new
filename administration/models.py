from django.db import models
from tinymce import HTMLField
# Create your models here.


class Administration(models.Model):
    title = models.CharField(max_length=254)
    content = HTMLField()


class page_image(models.Model):
    administartion = models.ForeignKey(Administration, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Administartion/", height_field=None, width_field=None, max_length=None)


class Administrative_Staff(models.Model):
    title = models.CharField(max_length=84)
    Post = models.CharField(max_length=254)
    administrative_offices = models.CharField(max_length=254)
    email = models.EmailField(blank=True)
    profile = models.ImageField(upload_to="Administartion/Desk_officials/", height_field=None, width_field=None, max_length=None)
from django.db import models
from tinymce import HTMLField

# Create your models here.
class Content(models.Model):
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=254)
    contact_info = models.TextField()
    logo_img = models.ImageField(upload_to="images/")
    header_text = models.CharField( max_length=254)


class Slider(models.Model):
    head = models.CharField(max_length=254)
    content = models.TextField()
    photo = models.ImageField(upload_to="slider/")


class Description(models.Model):
    header = models.CharField(max_length=254)
    content = models.TextField()


class Message_From_Chief(models.Model):
    chief_name = models.CharField(max_length=254)
    message = models.TextField()
    image = models.ImageField(upload_to="chiefs/", height_field=None, width_field=None, max_length=None)


class FAQ(models.Model):
    question = models.TextField()
    answer = HTMLField()

class aboutUs(models.Model):
    content = HTMLField()
    image1 = models.ImageField( upload_to="aboutus/", height_field=None, width_field=None, max_length=None)
    image2 = models.ImageField( upload_to="aboutus/", height_field=None, width_field=None, max_length=None)
    image3 = models.ImageField( upload_to="aboutus/", height_field=None, width_field=None, max_length=None)

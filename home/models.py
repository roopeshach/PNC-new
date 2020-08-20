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
    message = HTMLField()
    image = models.ImageField(upload_to="chiefs/", height_field=None, width_field=None, max_length=None)


class Campus_Chiefs_to_date(models.Model):
    chief_name = models.CharField(max_length=254)
    duration = models.CharField(max_length=254)


class FAQ(models.Model):
    question = models.TextField()
    answer = HTMLField()


class aboutUs(models.Model):
    content = HTMLField()
    image = models.ImageField( upload_to="aboutus/", height_field=None, width_field=None, max_length=None)


class PageImage(models.Model):
    about = models.ForeignKey(aboutUs, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="aboutus/")

    def __str__(self):
        return self.about.content


class SocialMedia(models.Model):
    facebook = models.CharField(blank=True, max_length=254)
    twitter = models.CharField( blank=True,max_length=254)
    google_plus = models.CharField(blank=True, max_length=254)
    linkedin = models.CharField(blank=True, max_length=254)
    youtube = models.CharField(blank=True, max_length=254)


class Preloader(models.Model):
    IS_ACTIVE = (
        ('T', 'Active'),
        ('F', 'In-Active'),
    )
    title = models.CharField(max_length=254)
    image = models.ImageField(upload_to="Preloader/", height_field=None, width_field=None, max_length=None)
    is_active = models.CharField(max_length=1, choices=IS_ACTIVE)

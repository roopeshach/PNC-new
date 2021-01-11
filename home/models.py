from django.db import models
from tinymce import HTMLField
from django.utils.html import mark_safe


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

    def SliderImage(self):
        return mark_safe('<img src="/media/%s" width="120" height="120" />' % self.photo)
        image_tag.short_description = self.head


class Description(models.Model):
    header = models.CharField(max_length=254)
    content = models.TextField()


class Message_From_Chief(models.Model):
    chief_name = models.CharField(max_length=254)
    message = HTMLField()
    image = models.ImageField(upload_to="chiefs/", height_field=None, width_field=None, max_length=None)

    def Image(self):
        return mark_safe('<img src="/media/%s" width="120" height="120" />' % self.image)
        image_tag.short_description = self.chief_name


class Campus_Chiefs_to_date(models.Model):
    chief_name = models.CharField(max_length=254)
    duration = models.CharField(max_length=254)

    def __str__(self):
        return self.chief_name


class FAQ(models.Model):
    question = models.TextField()
    answer = HTMLField()


class aboutUs(models.Model):
    content = HTMLField()
    image = models.ImageField( upload_to="aboutus/", height_field=None, width_field=None, max_length=None)

    def __str__(self):
        aboutus = "History and Development of Prithivi Narayan Campus"
        return aboutus


class PageImage(models.Model):
    about = models.ForeignKey(aboutUs, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="aboutus/")

    def __str__(self):
        image_title = "Images related to Prithivi Narayan Campus"
        return image_title


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

    def __str__(self):
        return self.title

    def Image(self):
        return mark_safe('<img src="/media/%s" width="120" height="120" />' % self.image)
        image_tag.short_description = self.title

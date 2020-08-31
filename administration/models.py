from django.db import models
from tinymce import HTMLField
from django.utils.text import slugify
# Create your models here.


class Administration(models.Model):
    title = models.CharField(max_length=254)
    content = HTMLField()

    def __str__(self):
        return self.title


class page_image(models.Model):
    administartion = models.ForeignKey(Administration, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Administartion/", height_field=None, width_field=None, max_length=None)


class Administrative_Staff(models.Model):
    name = models.CharField(max_length=84)
    Post = models.CharField(max_length=254)
    administrative_offices = models.CharField(max_length=254)
    email = models.EmailField(blank=True)
    profile = models.ImageField(upload_to="Administartion/Desk_officials/", height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name


class alumni(models.Model):
    IS_ACTIVE = (
        ('T', 'Active'),
        ('F', 'In-Active'),
    )
    title = models.CharField(max_length=254)
    content = HTMLField()
    is_active = models.CharField(max_length=1, choices=IS_ACTIVE)


    def __str__(self):
        return self.title


class alumni_images(models.Model):
    alumni_img = models.ForeignKey(alumni, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Alumni/", height_field=None, width_field=None, max_length=None)


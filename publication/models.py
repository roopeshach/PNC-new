from django.db import models
from category.models import Department, Program
from tinymce import HTMLField
from django.utils.text import slugify


# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=254)
    content = HTMLField()
    date = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, default=0, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, default=0, blank=True)
    feature_image = models.ImageField( upload_to="Publication/", blank=True, null=True)
    file = models.FileField(upload_to="Publication_file/", blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.date) + "-" + slugify(self.title)
        super(Publication, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class PublicationImage(models.Model):
    publication = models.ForeignKey(Publication,  on_delete = models.CASCADE)
    image = models.ImageField( upload_to="Publication/")

    def __str__(self):
        return self.publication.title
#
# class GoverningBody:



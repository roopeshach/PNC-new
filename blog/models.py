from django.db import models
from tinymce import HTMLField
from django.utils.text import slugify


# Create your models here.
class Blog(models.Model):
    IS_ACTIVE = (
        ('T', 'Active'),
        ('F', 'In-Active'),
    )
    title = models.CharField(max_length=254)
    content = HTMLField()
    date = models.DateTimeField()
    by = models.CharField(max_length=254)
    feature_image = models.ImageField(upload_to="Blogs/", height_field=None, width_field=None, max_length=None)
    is_active = models.CharField(max_length=1, choices=IS_ACTIVE)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.date) + "-" + slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class International_Relation(models.Model):
    IS_ACTIVE = (
        ('T', 'Active'),
        ('F', 'In-Active'),
    )
    header = models.CharField(max_length=254)
    content = HTMLField()
    image = models.ImageField(upload_to="International_relation/", height_field=None, width_field=None, max_length=None)
    is_active = models.CharField(max_length=1, choices=IS_ACTIVE)


class PageImage(models.Model):
    international_relation = models.ForeignKey(International_Relation, on_delete=models.CASCADE)
    image = models.ImageField( upload_to="International_Relation/")

    def __str__(self):
        return self.international_relation.header


class QAA(models.Model):
    title = models.CharField(max_length=254)
    content = HTMLField()
    QAA_Certificate = models.ImageField(upload_to="QAA/", height_field=None, width_field=None, max_length=None)
    EMIS_Report = models.FileField(upload_to="QAA/Report/", max_length=100)
    Strategic_Plan = models.FileField(upload_to="QAA/Report/", max_length=100)
    contact = HTMLField()

    def __str__(self):
        return self.title
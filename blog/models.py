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

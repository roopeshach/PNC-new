from django.db import models
from django.utils.text import slugify
from tinymce import HTMLField



# Create your models here.
class Faculty(models.Model):
    IS_ACTIVE = (
        ('T', 'Active'),
        ('F', 'In-Active'),
    )
    name = models.CharField(max_length=100)
    dean = models.CharField(max_length=100)
    dean_image = models.ImageField(upload_to='faculty/dean/')
    header = models.CharField(max_length=254)
    content = HTMLField()
    feature_image = models.ImageField(upload_to='faculty/')
    is_active = models.CharField(max_length=1, choices=IS_ACTIVE)

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Program, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Institute(models.Model):
    IS_ACTIVE = (
        ('T', 'Active'),
        ('F', 'In-Active'),
    )
    name = models.CharField(max_length=100)
    dean = models.CharField(max_length=100)
    dean_image = models.ImageField(upload_to='faculty/dean/')
    header = models.CharField(max_length=254)
    content = HTMLField()
    feature_image = models.ImageField(upload_to='faculty/')
    is_active = models.CharField(max_length=1, choices=IS_ACTIVE)

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Program, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Department(models.Model):
    IS_ACTIVE = (
        ('T', 'Active'),
        ('F', 'In-Active'),
    )
    name = models.CharField(max_length=100)
    dean = models.CharField(max_length=100)
    dean_image = models.ImageField(upload_to='department/dean/')
    header = models.CharField(max_length=254)
    content = HTMLField()
    feature_image = models.ImageField(upload_to='department/feature/')
    is_active = models.CharField(max_length=1, choices=IS_ACTIVE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE , null=True, default=0, blank=True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE , null=True, default=0, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Department, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Program(models.Model):
    IS_ACTIVE = (
        ('T', 'Active'),
        ('F', 'In-Active'),
    )
    name = models.CharField(max_length=100)
    dean = models.CharField(max_length=100)
    dean_image = models.ImageField(upload_to='program/dean/')
    header = models.CharField(max_length=254)
    content = HTMLField()
    feature_image = models.ImageField(upload_to='program/feature/')
    is_active = models.CharField(max_length=1, choices=IS_ACTIVE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, default=0, blank=True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, null=True, default=0, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Program, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Custom_Page(models.Model):
    IS_ACTIVE = (
        ('T', 'Active'),
        ('F', 'In-Active'),
    )

    name = models.CharField(max_length=254)
    header = models.CharField(max_length=254)
    content = HTMLField()
    image = models.ImageField(upload_to="custom_pages/", height_field=None, width_field=None, max_length=None)

    is_active = models.CharField(max_length=1, choices=IS_ACTIVE)

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Custom_Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

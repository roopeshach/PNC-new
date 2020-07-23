from django.db import models
from category.models import Department, Program
from tinymce import HTMLField
from django.utils.text import slugify


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=254)
    content = HTMLField()
    date = models.DateTimeField()
    feature_image = models.ImageField( upload_to="events/", height_field=None, width_field=None, max_length=None)
    slug = models.SlugField(blank=True)

    file = models.FileField(upload_to="events_file/", blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.date) + "-" + slugify(self.title)
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=254)
    content = HTMLField()
    date = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, default=0, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, default=0, blank=True)
    feature_image = models.ImageField( upload_to="news/", blank=True, null=True)

    file = models.FileField(upload_to="news_file/", blank=True, null=True)

    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.date) + "-" + slugify(self.title)
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Notice(models.Model):
    title = models.CharField(max_length=254)
    content = HTMLField()
    date = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, default=0, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, default=0, blank=True)
    feature_image = models.ImageField( upload_to="notice/", height_field=None, width_field=None, max_length=None)

    file = models.FileField(upload_to="notice_file/", blank=True, null=True)

    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.date) + "-" + slugify(self.title)
        super(Notice, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    news = models.ForeignKey(News,  on_delete=models.CASCADE)
    image = models.ImageField( upload_to="news/")

    def __str__(self):
        return self.news.title


class NoticeImage(models.Model):
    notice = models.ForeignKey(Notice,  on_delete=models.CASCADE)
    image = models.ImageField( upload_to="notice/")

    def __str__(self):
        return self.notice.title


class EventImage(models.Model):
    event = models.ForeignKey(Event,  on_delete=models.CASCADE)
    image = models.ImageField( upload_to="event/")

    def __str__(self):
        return self.event.title

    
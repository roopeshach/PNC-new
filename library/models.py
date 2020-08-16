from django.db import models

# Create your models here.


class E_Resources(models.Model):
    title = models.CharField(max_length=254)
    link = models.CharField(max_length=254)

from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField( max_length=254)
    title = models.CharField( max_length=250)
    comment = models.TextField()

    date = models.DateTimeField(auto_now_add=True)
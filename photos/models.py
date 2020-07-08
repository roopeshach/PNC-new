from django.db import models
from category.models import Department , Program
# Create your models here.
class DepartmentImage(models.Model):
    image_title = models.CharField( max_length=254)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.department)


class DepartmentGallery(models.Model):
    title = models.ForeignKey(DepartmentImage ,on_delete=models.CASCADE)
    image = models.ImageField( upload_to="gallery/department/")

    def __str__(self):
        return self.title.image_title

class ProgramImage(models.Model):
    image_title = models.CharField( max_length=254)
    program = models.ForeignKey(Program,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.program)


class ProgramGallery(models.Model):
    title = models.ForeignKey(ProgramImage ,on_delete=models.CASCADE)
    image = models.ImageField( upload_to="gallery/program/")

    def __str__(self):
        return self.title.image_title
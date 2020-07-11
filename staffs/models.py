from django.db import models
from category.models import Department, Program
# Create your models here.
class Staff(models.Model):
    IS_ACTIVE = (
        ('T', 'True'),
        ('F', 'False'),
    )
    name = models.CharField( max_length=100)
    address = models.CharField( max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=12)
    # department = models.ForeignKey(Department, blank=True,null=True, on_delete=models.CASCADE)
    department = models.ManyToManyField(Department)
    program = models.ForeignKey(Program, blank=True, null=True,on_delete=models.CASCADE)
    role = models.CharField(max_length=100, blank=True)
    admin_role = models.CharField(max_length=50, blank=True)
    
    image = models.ImageField( upload_to="staffs/", height_field=None, width_field=None, max_length=None)
    biodata = models.FileField(upload_to="staffs_file", max_length=200)


    is_active = models.CharField(max_length=1, choices=IS_ACTIVE)

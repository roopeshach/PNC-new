from django.db import models


# Create your models here.

class governing_body_desc(models.Model):
    title = models.CharField(max_length=250)
    desc = models.TextField()

    def __str__(self):
        return self.title


class management_committee_desc(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()


class executive_committee_desc(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()


class campus_authority_desc(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()


class Management_committee_members(models.Model):
    name = models.CharField(max_length=50)
    member_role = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    profile_image = models.ImageField(upload_to="governing_bodies/MC/")


class Executive_committee_members(models.Model):
    name = models.CharField(max_length=50)
    member_role = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    profile_image = models.ImageField(upload_to="governing_bodies/EC/")


class Campus_Authorities_members(models.Model):
    name = models.CharField(max_length=50)
    department_or_faculty = models.CharField(max_length=250, blank=True)
    member_role = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    profile_image = models.ImageField(upload_to="governing_bodies/CA/")


class First_Management_committee(models.Model):
    member_role = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    work_as = models.CharField(max_length=250)

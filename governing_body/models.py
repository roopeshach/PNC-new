from django.db import models


# Create your models here.
# class committee(models.Model):
#     committee_name = models.CharField(max_length=100)
#     year = models.CharField(max_length=100)


# class committee_role(models.Model):
#     active = (
#         ("True","True"),
#         ("False", 'False'),
#     )
#     role_name = models.CharField(max_length=100)
#     committee_name = models.ForeignKey(committee, on_delete=models.CASCADE)
#     is_active = models.CharField(max_length=10, choices=active)


# class committee_member(models.Model):
#     active = (
#         ("True", "True"),
#         ("False", 'False'),
#     )
#     name = models.CharField(max_length=100)
#     committee = models.ForeignKey(committee, on_delete=models.CASCADE)
#     is_active = models.CharField(max_length=10,choices=active)


class governing_body_desc(models.Model):
    title = models.CharField( max_length=250)
    desc = models.TextField()

    def __str__(self):
        return self.title

class management_committee_desc(models.Model):
    name = models.CharField( max_length=50)
    desc = models.TextField()

class executive_committee_desc(models.Model):
    name = models.CharField( max_length=50)
    desc = models.TextField()

class campus_authority_desc(models.Model):
    name = models.CharField( max_length=50)
    desc = models.TextField()


class Management_committee_members(models.Model):
    name = models.CharField( max_length=50)
    member_role = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    profile_image = models.ImageField(upload_to="governing_bodies/MC/")

class Executive_committee_members(models.Model):
    name = models.CharField( max_length=50)
    member_role = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    profile_image = models.ImageField(upload_to="governing_bodies/EC/")

class Campus_Authorities_members(models.Model):
    name = models.CharField( max_length=50)
    member_role = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    profile_image = models.ImageField(upload_to="governing_bodies/CA/")


    
    
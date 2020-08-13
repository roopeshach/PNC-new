from django.db import models


# Create your models here.
class committee(models.Model):
    committee_name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)


class committee_role(models.Model):
    active = (
        ("True","True"),
        ("False", 'False'),
    )
    role_name = models.CharField(max_length=100)
    committee_name = models.ForeignKey(committee, on_delete=models.CASCADE)
    is_active = models.CharField(max_length=10, choices=active)


class committee_member(models.Model):
    active = (
        ("True", "True"),
        ("False", 'False'),
    )
    name = models.CharField(max_length=100)
    committee = models.ForeignKey(committee, on_delete=models.CASCADE)
    is_active = models.CharField(max_length=10,choices=active)

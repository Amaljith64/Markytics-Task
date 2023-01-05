from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class IncidentReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=225)
    department = models.TextField(null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    incident_location = models.TextField(null=True)
    initial_severity = models.CharField(max_length=225, null=True)
    suspected_cause = models.TextField(null=True)
    immediate_action = models.TextField(null=True)

    def __str__(self):
        return self.user.username


class SubIncidentTypes(models.Model):
    typeof = models.ForeignKey(IncidentReport, on_delete=models.CASCADE)
    type = models.CharField(max_length=225)

    def __str__(self):
        return self.typeof.location

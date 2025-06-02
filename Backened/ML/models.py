from django.db import models

# Create your models here.
class Approvalmodel(models.Model):
    Program=models.CharField(max_length=50)
    Level=models.CharField(max_length=50)
    Courses=models.IntegerField()
    Intake=models.IntegerField()
    Maximum=models.IntegerField()
    Division=models.IntegerField()
    Email=models.EmailField(max_length=50,null=True, blank=True)
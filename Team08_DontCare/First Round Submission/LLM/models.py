from django.db import models

# Create your models here.
class Output(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=250,null=True)
    authors=models.TextField(null=True)
    alt=models.CharField(max_length=250,null=True)
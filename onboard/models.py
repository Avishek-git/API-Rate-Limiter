from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    endpoint = models.CharField(max_length=100,primary_key=True)
    rate_limit = models.PositiveIntegerField()
    custom_endpoint = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.endpoint
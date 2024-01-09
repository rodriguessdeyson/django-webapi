from django.db import models
from .componentModel import Component

# Create your models here.
class Manufacturer(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50, null = True, blank = True)
    part_number = models.CharField(max_length = 50, null = True, blank = True)
    datasheet = models.BinaryField(null = True)
    component = models.ForeignKey(Component, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Manufacturers"
        ordering = ["name"]
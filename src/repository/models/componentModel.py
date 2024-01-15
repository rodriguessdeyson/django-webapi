from django.db import models

# Create your models here.

class Component(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    type = models.SmallIntegerField()
    description = models.CharField(max_length = 250)
    aqtech_part_number = models.CharField(max_length = 100)
    foot_print = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.name} - {self.aqtech_part_number}"
    
    class Meta:
        db_table = "Components"
        ordering = ["id"]
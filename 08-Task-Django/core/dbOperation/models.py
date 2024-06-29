from django.db import models

class ExcelModel(models.Model):
    parameter_name = models.CharField(max_length=100)
    machine_name = models.CharField(max_length=100)
    value = models.FloatField()
    yesterday_date = models.CharField(max_length=100)
    def __str__(self):
        return f"id: {self.id} - {self.column_b}"

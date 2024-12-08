from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    calories = models.FloatField()
    protein_content = models.FloatField()
    carbohydrate_content = models.FloatField()
    fat_content = models.FloatField()
    # Diğer alanlar...

    def __str__(self):
        return self.name
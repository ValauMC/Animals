from django.db import models

# Create your models here.
class Species(models.Model):
    name = models.CharField(max_length=255)

class Animals(models.Model):
    name = models.CharField(max_length=255)
    natural_habitat = models.CharField(max_length=255)
    life_expectancy = models.CharField(max_length=255)
    image_url = models.URLField(max_length=255, blank=True, null=True)
    specie = models.ForeignKey(Species, on_delete=models.CASCADE)

class Behavior(models.Model):
    social_behavior = models.CharField(max_length=255)
    actividad = models.CharField(max_length=255)
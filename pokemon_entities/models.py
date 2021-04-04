from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    title_jp = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(null=True)
    description = models.TextField(blank=True, null=True)
    previous_evolution = models.ForeignKey('self', on_delete=models.CASCADE,
                                           related_name='next_evolution',
                                           blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.title_ru)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey('Pokemon', on_delete=models.CASCADE, blank=True, null=True)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Appeared_at = models.DateTimeField(blank=True, null=True)
    Disappeared_at = models.DateTimeField(blank=True, null=True)
    Level = models.IntegerField(blank=True, null=True)
    Health = models.IntegerField(blank=True, null=True)
    Strength = models.IntegerField(blank=True, null=True)
    Defence = models.IntegerField(blank=True, null=True)
    Stamina = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.pokemon)

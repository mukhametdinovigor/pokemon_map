from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Русское название покемона')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='Английское название покемона')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='Японское название покемона')
    image = models.ImageField(null=True, verbose_name='Изображение покемона')
    description = models.TextField(blank=True, verbose_name='Описание покемона')
    previous_evolution = models.ForeignKey('self', on_delete=models.SET_NULL,
                                           related_name='next_evolution',
                                           blank=True, null=True, verbose_name='Предыдущая эволюция покемона')

    def __str__(self):
        return '{}'.format(self.title_ru)


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey('Pokemon', on_delete=models.CASCADE,
                                related_name='pokemon_entity',
                                blank=True, null=True, verbose_name='Название покемона')
    Latitude = models.FloatField(verbose_name='Широта')
    Longitude = models.FloatField(verbose_name='Долгота')
    Appeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Появляется в')
    Disappeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Исчезает в')
    Level = models.IntegerField(blank=True, null=True, verbose_name='Уровень')
    Health = models.IntegerField(blank=True, null=True, verbose_name='Здоровье')
    Strength = models.IntegerField(blank=True, null=True, verbose_name='Сила')
    Defence = models.IntegerField(blank=True, null=True, verbose_name='Защита')
    Stamina = models.IntegerField(blank=True, null=True, verbose_name='Выносливость')

    def __str__(self):
        return '{}'.format(self.pokemon)

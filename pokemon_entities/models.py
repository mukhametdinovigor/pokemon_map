from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200)
    image = models.ImageField(null=True)

    def __str__(self):
        return '{}'.format(self.title_ru)

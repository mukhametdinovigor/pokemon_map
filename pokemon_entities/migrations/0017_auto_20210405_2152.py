# Generated by Django 3.1.7 on 2021-04-05 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0016_auto_20210405_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_entity', to='pokemon_entities.pokemon', verbose_name='Название покемона'),
        ),
    ]

import folium

from django.shortcuts import render
from pokemon_entities.models import PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons_on_page = []
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in PokemonEntity.objects.all():
        add_pokemon(
            folium_map, pokemon.Latitude, pokemon.Longitude, request.build_absolute_uri(pokemon.pokemon.image.url))
        pokemons_on_page.append({
            'pokemon_id': pokemon.pokemon.id,
            'img_url': request.build_absolute_uri(pokemon.pokemon.image.url),
            'title_ru': pokemon.pokemon.title_ru,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = PokemonEntity.objects.get(id=pokemon_id)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    add_pokemon(
        folium_map, pokemon.Latitude, pokemon.Longitude, request.build_absolute_uri(pokemon.pokemon.image.url))

    pokemon_on_page = {
        'pokemon_id': pokemon.pokemon.id,
        'img_url': request.build_absolute_uri(pokemon.pokemon.image.url),
        'title_ru': pokemon.pokemon.title_ru,
        'title_en': pokemon.pokemon.title_en,
        'title_jp': pokemon.pokemon.title_jp,
        'description': pokemon.pokemon.description
    }

    if pokemon.pokemon.previous_evolution:
        pokemon_on_page['previous_evolution'] = {
            'title_ru': pokemon.pokemon.previous_evolution.title_ru,
            'pokemon_id': pokemon.pokemon.previous_evolution.id,
            'img_url': request.build_absolute_uri(pokemon.pokemon.previous_evolution.image.url)
        }
    try:
        if pokemon.pokemon.next_evolution.all()[0]:
            pokemon_on_page['next_evolution'] = {
                'title_ru': pokemon.pokemon.next_evolution.all()[0].title_ru,
                'pokemon_id': pokemon.pokemon.next_evolution.all()[0].id,
                'img_url': request.build_absolute_uri(pokemon.pokemon.next_evolution.all()[0].image.url)
            }
    except IndexError:
        pass

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon_on_page})

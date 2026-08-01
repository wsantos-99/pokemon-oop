import random
import data.pokemons_data as pokemons_data
from models.trainer import Trainer


def get_pokemons_by_level(level):
    available_pokemons = []

    for pokemon_name, pokemon_data in pokemons_data.POKEMONS.items():
        min_level, max_level = pokemon_data["wild_level_range"]

        if min_level <= level <= max_level:
            available_pokemons.append(pokemon_name)
    print(f"{available_pokemons}")
    return available_pokemons


def pokemon_create(trainer):
    player_level = trainer._level

    level = random.randint(max(1, player_level - 3), min(100, player_level + 2))

    available_pokemons = get_pokemons_by_level(level)

    if not available_pokemons:
        return None

    pokemon_name = random.choice(available_pokemons)

    print(f"Pokémon: {pokemon_name} (Lv {level})")

    return pokemon_name, level


player = Trainer("player")
player._level = 65

pokemon_create(player)


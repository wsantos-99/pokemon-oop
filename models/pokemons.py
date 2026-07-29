import data.pokemons_data as pokemons_data



class Pokemon:
    def __init__(self, pokemon, name="", level=1):
        pokemon = pokemons_data.POKEMONS[pokemon]

        if name:
            self._name = name
        else:
            self._name = ""

        self._species = pokemon["species"]
        self._types = pokemon["types"]
        self._level = level

        self._hp = pokemon["hp"]
        self._attack = pokemon["attack"]
        self._defense = pokemon["defense"]
        self._speed = pokemon["speed"]

        self._experience = pokemon["experience"]
        self._xp_to_next_level = pokemon["xp_to_next_level"]
        self._evolves_to = pokemon["evolves_to"]
        self._evolution_level = pokemon["evolution_level"]
        self._moves = pokemon["moves"]

    def __str__(self):
        if self._name != "":
            return f"{self._name} {self._species} {self._level}"
        else:
            return f"{self._species} {self._level}"




teste1 = Pokemon("Charmander")
teste2 = Pokemon("Charmander", name="nick")
teste3 = Pokemon("Charmander", name="nick", level=10)
print(teste1)
print(teste2)
print(teste3)




























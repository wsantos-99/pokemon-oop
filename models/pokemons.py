import data.pokemons_data as pokemons_data
import random



class Pokemon:
    def __init__(self, pokemon, name="", level=1, iv=0.1):
        pokemon = pokemons_data.POKEMONS[pokemon]
        self._data = pokemon
        if name:
            self._name = name
        else:
            self._name = pokemon["species"]

        self._species = pokemon["species"]
        self._types = pokemon["types"]
        self._level = level
        self._iv = 1 + iv

        self._hp = pokemon["hp"]
        self._attack = pokemon["attack"]
        self._defense = pokemon["defense"]
        self._speed = pokemon["speed"]
        self._moves = pokemon["moves"]

    def __str__(self):
        if self._name != "":
            return f"{self._name} {self._species} {self._level}"
        else:
            return f"{self._species} {self._level}"


class WildPokemon(Pokemon):
    def __init__(self, pokemon, name="", level=1):
        super().__init__(pokemon, level=level)
        self._iv = random.uniform(0.1, 0.4)


class PlayerPokemon(Pokemon):
    def __init__(self, pokemon, name="", level=1, iv=1):
        super().__init__(pokemon, name, level, iv)

        self._experience = 0
        self._xp_to_next_level = 100
        self._evolves_to = self._data["evolves_to"]
        self._evolution_level = self._data["evolution_level"]


    def evolve(self):
        print(f"{self._name} evolves to {self._evolves_to}")
        self._data = pokemons_data.POKEMONS[self._evolves_to]

        self._species = self._data["species"]
        self._types = self._data["types"]

        self._hp = self._data["hp"] * self._iv
        self._attack = self._data["attack"] * self._iv
        self._defense = self._data["defense"] * self._iv
        self._speed = self._data["speed"] * self._iv
        self._moves = self._data["moves"]

        self._evolves_to = self._data["evolves_to"]
        self._evolution_level = self._data["evolution_level"]


    def level_up(self, level):
        self._level += level

    def get_total_experience(self):
        total_xp = self._experience
        for level in range(1, self._level):
            total_xp += level * 100

        return total_xp

    def show_experience_gain(self, experience):
        max_xp = 495000
        total_experience = self.get_total_experience()

        if total_experience + experience >= max_xp:
            print(f"{self._name} gain {max_xp - total_experience} experience")
        else:
            print(f"{self._name} gain {experience} experience")

    def gain_experience(self, experience):
        if self._level < 100:
            partial_level = 0
            self.show_experience_gain(experience)
            self._experience += experience

            if self._experience >= 100:
                print("Level up!")
                while self._experience >= self._xp_to_next_level:
                    self._experience -= self._xp_to_next_level
                    partial_level += 1
                    self._xp_to_next_level += 100
                    if partial_level + self._level >= 100:
                        break
                self.level_up(partial_level)
                print(f"{self._name} has just reached Level {self._level}")

                if self._level >= self._evolution_level:
                    while self._evolution_level and self._level >= self._evolution_level:
                        self.evolve()






charmander = PlayerPokemon("Charmander", name="Charmander", level=1, iv=0.2)
charmander.gain_experience(4000000000000000000000000000)





























from functools import partial


class Trainer:
    def __init__(self, name):
        self._name = name
        self._level = 1
        self._xp = 0

        self._pokemons = {}
        self._pokeballs = {}
        self._items = {}
        self._badges = []

        self._gold = 0


    # trainer functions

    def level_up(self, level):
        self._level += level

    def gain_experience(self, experience):
        print(f"you gain {experience} experience")
        partial_level = 0
        self._xp += experience
        if self._xp >= 100:
            while self._xp >= 100:
                self._xp -= 100
                partial_level += 1
                print("Level up!")
            self.level_up(partial_level)
            print(f"You have just reached Level {self._level}")


    # pokemons functions

    def add_pokemon(self, pokemon):
        pass

    def remove_pokemon(self, pokemon):
        pass

    def get_pokemons(self):
        pass


    # items functions

    def add_item(self, item, amount):
        if self._items.__contains__(item):
            self._items[item] += amount
        else:
            self._items[item] = amount
        print(f"you have added {amount} {item} to your inventory")


    def remove_item(self, items):
        pass

    def show_items(self):
        for item, amount in self._items.items():
            print(item, amount)

    def add_pokeball(self, pokeball):
        pass

    def remove_pokeball(self, pokeball):
        pass


    # badges functions

    def add_badge(self, badge):
        self._badges.append(badge)
        print(f"You have earned the Badge: {badge}")

    def count_badges(self):
        print(f"you have {len(self._badges)} Badges")

    def show_badges(self):
        self.count_badges()
        for badge in self._badges:
            print(badge)


    # gold functions

    def add_gold(self, gold):
        self._gold += gold
        print(f"you received {gold} gold")

    def remove_gold(self, gold):
        self._gold -= gold
        print(f"You lost {gold} gold")

    def show_gold(self):
        print(f"you have {self._gold} gold")


player = Trainer("player")
player.gain_experience(300)
player.add_badge("macaco")
player.add_badge("pato")
player.show_badges()
player.add_gold(12)
player.remove_gold(1)
player.show_gold()
player.add_item("churrasco", 2)
player.add_item("churrasco", 1)
player.add_item("sco", 2)
player.show_items()
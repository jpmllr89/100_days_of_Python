class Item:
    def __init__(self, name):
        self.name = name


class Medicine(Item):
    def __init__(self, name, health):
        super().__init__(name)
        self.health = Health

    def take(hero):
        hero.health += self.health

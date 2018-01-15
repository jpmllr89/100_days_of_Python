class Item:
    def __init__(self, name):
        self.name = name

    def add_inventory(hero):
        hero.inventory.append(self.name)


class Medicine(Item):
    def __init__(self, name, health):
        super().__init__(name)
        self.health = health

    def take(hero):
        hero.health += self.health


class Weapon(Item):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage

    def equip(hero):
        hero.body["right_hand"] = self.name
        hero.strength +=damage

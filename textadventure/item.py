class Item:
    def __init__(self, name, sell, buy):
        self.name = name
        self.sell = sell
        self.buy = buy


    def add_inventory(hero):
        hero.inventory.append(self.name)


class Medicine(Item):
    def __init__(self, name, sell, buy, health):
        super().__init__(name, sell, buy)
        self.health = health

    def take(hero):
        hero.health += self.health


class Weapon(Item):
    def __init__(self, name, sell, buy, damage):
        super().__init__(name, sell, buy)
        self.damage = damage

    def equip(hero):
        hero.body["right_hand"] = self.name
        hero.strength +=damage

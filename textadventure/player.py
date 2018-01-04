class Player:
    def __init__(self, name, strength, health):
        self.inventory = []
        self.name = name
        self.strength = strength
        self.health = health

    def add_to_inventory(self, obj):
        self.inventory.append(obj)

    def list_inventory(self):
        print("Here is the inventory in " + self.name +"'s"+" inventory:")
        print()
        for i in self.inventory:
            print(i)
            print()

    def give_item(self, person, obj):
        person.inventory.append(obj)
        self.inventory.remove(obj)
        print(self.name+" gave " + obj + " to " + person.name)

    def attack(self):
        attack = random.randint(0,2) * self.strength
        print(attack)

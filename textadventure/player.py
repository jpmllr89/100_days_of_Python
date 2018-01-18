class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, opponent):
        attack = 1
        opponent.health -= 1

    def evade(self):
        randInt = random.random()
        if randInt >.4:
            return False

# Hero extends the Player super class
class Hero(Player):
    def __init__(self, name, health, strength, gold):
        super().__init__(name, health)
        # this is an equipment dictionary.
        self.inventory = []
        self.strength = strength
        self.gold = 0

    def add_to_inventory(self, obj):
        print("You have taken the "+ obj)
        self.inventory.append(obj)

    def list_inventory(self):
        if len(self.inventory) ==0:
            print("there is nothing in here")
        print("Here is the inventory in " + self.name +"'s"+" inventory:")
        print()
        for i in self.inventory:
            print(i)

    def give_item(self, person, obj):
        person.inventory.append(obj)
        self.inventory.remove(obj)
        print(self.name+" gave " + obj + " to " + person.name)

    def pay(self, amount):
        if self.gold-amount <=0:
            print("You cannot afford this!")
        else:
            self.gold-=amount
            print("You have "+str(self.gold)+" left.")
            return True

# Villain extends the Player superclass
class Villain(Player):
    def __init__(self, name, health, gold):
        super().__init__(name, health)
        self.gold = gold

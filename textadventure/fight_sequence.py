import random

def protag_turn(villain):
    ask = input("What will you do? (attack/run)")
    if ask =="run":
        chance = random.random()
        if chance > 0.5:
            print("Bye Felicia!")
            going_on = False
        else:
            print("You stumble and "+ villain.name +" attacks!")

    elif ask =="attack":
        print("BOOM")
        villain.health -=1
        print(villain.health)
        if villain.health ==0:
            going_on = False

def antag_turn(hero):
    hero.health -=1
    if hero.health == 0:
        going_on = False
    print(hero.health)

def fight_seq(villain, hero):
    going_on = True
    count = villain.health
    print(villain.name + " approaches!")
    while(going_on):
        protag_turn(villain)
        antag_turn(hero)

#need to work on sequence, not like a real rpg where there are turns.

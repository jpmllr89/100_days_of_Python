import random
from bestiary import *

def protag_turn(hero, villain):
    ask = input("What will you do? (attack/run)")
    turn = True
    while(turn):
        if ask == "run":
            turn = False
            return run()
        elif ask == "attack":
            print("BOOM")
            villain.health -=1
            print(villain.health)
            turn = False

def antag_turn(hero, villain):
    turn = True
    print(villain.name + " attacks!")
    while(turn):
        if check_evasion(hero) ==True:
            print(hero.name + " evaded the attack!")
        else:
            hero.health -=1
            print(hero.health)
        turn = False

# checks to see if protagonist evades attack
def check_evasion(player):
    chance = random.random()
    print(chance)
    if chance > .8:
        return True

def run():
    chance = random.random()
    if chance > 0.5:
        print("You ran away!")
        return True


# checks to see if any party is dead.
def check_death(hero, villain):
    if hero.health == 0:
        print("You died!")
        return True
    if villain.health == 0:
        print("You have killed " + villain.name+ "!")
        return True

def fight_seq(hero, villain):
    going_on = True
    print(villain.name + " approaches!")
    while(going_on):
        if check_death(hero, villain) == True:
            break
        if run()==True:
            break
        protag_turn(hero, villain)
        antag_turn(hero, villain)


fight_seq(bestiary["Fly"], bestiary["Pencil"])

#need to work on sequence, not like a real rpg where there are turns.

import random
from bestiary import *

def goes_first():
    coin = random.randInt(1,2)
    if coin == 1:
        return True

# we should probably put this into its own class later on.
def run():
    print("You ran away successfully!")
    return True

def protag_turn(hero, villain):
    ask = input("What will you do? (attack/run)")
    if ask == "run":
        run()
    elif ask == "attack":
        print("BOOM")
        villain.health -=1
        print(villain.health)
    else:
        protag_turn(hero, villain)

def antag_turn(hero, villain):
    print(villain.name + " attacks!")
    hero.health -=1
    print(hero.health)

    # while(turn):
    #     if check_evasion(hero) ==True:
    #         print(hero.name + " evaded the attack!")
    #     else:
    #         hero.health -=1
    #         print(hero.health)
    #     turn = False

# checks to see if protagonist evades attack
# def check_evasion(player):
#     chance = random.random()
#     print(chance)
#     if chance > .8:
#         return True

# def run():
#     chance = random.random()
#     if chance > 0.5:
#         print("You ran away!")
#         return True


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
        protag_turn(hero, villain)
        if run() == True:
            break
        antag_turn(hero, villain)

fight_seq(bestiary["Fly"], bestiary["Pencil"])

#need to work on sequence, not like a real rpg where there are turns.

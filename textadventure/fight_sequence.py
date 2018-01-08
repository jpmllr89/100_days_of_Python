import random
from bestiary import *
import time
import sys

# ran_away = False
# def run():
#     chance = random.random()
#     if chance < 0.5:
#         print("False")
#         return False
#     else:
#         print("True")
#         return True

# checks to see if protagonist evades attack
# def check_evasion(player):
#     chance = random.random()
#     print(chance)
#     if chance > .8:
#         return True

def check_death(player):
    if player.health == 0:
        return True

def protag_turn(hero, villain):
    ask = input("What will you do? (attack/inventory)")
    if ask == "attack":
        print("BOOM")
        villain.health -=1

    else:
        print("You've got to do something!")
        protag_turn(hero, villain)

def antag_turn(hero, villain):
    print(villain.name + " attacks!")
    hero.health -=1
    print("Your Health: "+ str(hero.health))
    # while(turn):
    #     if check_evasion(hero) ==True:
    #         print(hero.name + " evaded the attack!")
    #     else:
    #         hero.health -=1
    #         print(hero.health)
    #     turn = False

# checks to see if any party is dead.

def fight_seq(hero, villain):
    going_on = True
    print(villain.name + " approaches!")
    while(going_on):
        protag_turn(hero, villain)
        if check_death(villain) ==True:
            print("You Won!")
            hero.gold += villain.gold
            print("You gained " + str(villain.gold)+ " gold!")
            break
        antag_turn(hero, villain)
        if check_death(hero) == True:
            print("You died!")
            going_on = False


# print(run())
# print(run())
# print(run())
# print(run())
# print(run())
#need to work on sequence, not like a real rpg where there are turns.

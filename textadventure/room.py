import random
from fight_sequence import *
from player import *
from bestiary import *
from locations import *
def game():
    print(""" You're walking down the school hall, second period is over and you
     have five minutes to get to third period before the hall monitors will
     yell at you for being late.
    """)
    decision = input("Where will you go? (bathroom/class/bleachers/cafeteria)")
    if decision == "bathroom":
        bathroom_scene()
    elif decision == "class":
        print("n")
    elif decision == "bleachers":
        print("n")
    elif decision == "cafeteria":
        print("n")


game()
# 20170102 - figured how to import dictionary.
# separated the fight sequence into another module

# fight_seq(bestiary["Fly"])

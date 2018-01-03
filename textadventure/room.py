import random
from fight_sequence import *
from player import *
from bestiary import *

def bathroom_scene():
    print("""You've entered the bathroom.
    There is a magnum condom next to the trashcan, the soap bottle is actually filled
    with urine, and it smells like some one was just smoking weed""")
    decision = input("What to do now? (wash hands/leave)")
    if decision.lower() =="wash hands":
        print("You wash your hands, and dare not to touch the soap bottle. gross.")
        print("""you look into the mirror and notice a crack.  The mirror is thinner and """)

def game():
    print(""" You're walking down the school hall, second period is over and you
     have five minutes to get to third period before the hall monitors will
     yell at you for being late.
    """)
    decision = input("Where will you go? (bathroom/class/bleachers/cafeteria)")
    if decision == "bathroom":
        print("n")
    elif decision == "class":
        print("n")
    elif decision == "bleachers":
        print("n")
    elif decision == "cafeteria":
        print("n")

fight_seq(bestiary["Fly"], bestiary["Pencil"])
# 20170102 - figured how to import dictionary.
# separated the fight sequence into another module

# fight_seq(bestiary["Fly"])

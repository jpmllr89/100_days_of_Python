import random
from player import *
import bestiary
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

# Should probs be another module below:
def fight_seq(villain):
    villain =villain
    going_on = True
    hp = villain.health
    print(villain.name + " approaches!")
    while(going_on):
        ask = input("What will you do? (attack/run)")
        if ask =="run":
            print("Bye Felicia!")
        elif ask =="attack":
            print("BOOM")
            hp -=1
            print(hp)
            if hp ==0:
                going_on = False

# apparently imported module is not subscriptable, i.e. the data that we try to
# import from the bestiary.py dictionary cannot be called.
# print(bestiary["Fly"].name)
# fight_seq(bestiary["Fly"])

import random
from fight_sequence import *
def bathroom_scene():
    print("""You've entered the bathroom.  Just a regular bathroom, but some of
    the 'bad kids' hangout here.  It smells like someone was smoking in here
    probably a couple of hours ago.""")
    in_area = True
    while(in_area):
        decision = input("What to do now? (wash hands/leave)")
        fight = random.random()
        if fight < .3:
            fight_seq()
        if decision.lower() =="wash hands":
            print("You wash your hands, and dare not to touch the soap bottle. gross.")
            print("""you look into the mirror and notice a crack.  The mirror is thinner and """)
        if decision.lower() == "leave":
            print("You have left the bathroom")
            in_area = False

def classroom_scene():
    print("""You walk into the class room where there are 20 desks arranged in a
    grid.  The teacher is at her desk and does not even notice you walking in.""")
    in_area = True
    while(in_area):
        decision = input("What to do now? (t for take a seat/b for bother teacher)")
        fight = random.random()
        if fight < .3:
            fight_seq()
        if decision.lower() =="t":
            print("You wash your hands, and dare not to touch the soap bottle. gross.")
            print("""you look into the mirror and notice a crack.  The mirror is thinner and """)
        if decision.lower() == "b":
            print("You have left the bathroom")
            in_area = False

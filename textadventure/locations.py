import random
from fight_sequence import *
import time



def bathroom_scene(hero):
    time.sleep(1)
    print("""You've entered the bathroom.  Just a regular bathroom, but some of
    the 'bad kids' hangout here.  It smells like someone was smoking in here
    probably a couple of hours ago.""")
    time.sleep(1)

    in_area = True
    while(in_area):
        decision = input("What to do now? (wash hands/leave)")
        fight = random.random()
        if fight < .3:
            fight_seq()
        if decision.lower() =="wash hands":
            print("You wash your hands, and dare not to touch the soap bottle....")
            time.sleep(1)
            print("gross....")
            time.sleep(1)
            if "key" not in hero.inventory:

                print("you look into the mirror and notice a crack....")
                time.sleep(1)
                print("The mirror is thinner and looks pliable.")
                time.sleep(1)
                print(""" You wouldn't expect to find anything of use hidden between
                 any cracks, but yet you're curious to see could be behind it...""")
                crack_open = input("Should you break a piece off?(y/n)")
                if crack_open.lower() == "y":
                    time.sleep(1)
                    print("A small file cabinet key falls out and nearly goes down the sink")
                    time.sleep(1)
                    print("""You quickly stick your fingers down the sink to prevent
                    the key from going down there""")
                    time.sleep(1)
                    hero.add_to_inventory("key")
                    hero.list_inventory()
                    time.sleep(1)
                    print("""While you dry off your hands you wonder where could this
                    key belong to?""")

            else:
                time.sleep(1)
                print("You quickly dry off your hands")

        if decision.lower() == "leave":
            print("You have left the bathroom")
            in_area = False

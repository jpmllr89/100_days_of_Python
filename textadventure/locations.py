import random
from fight_sequence import *
import time

def init_fight(hero):
    fight = random.random()
    if fight < .3:
        enemy = bestiary[str(random.choice(list(bestiary.items()))[0])]
        fight_seq(hero, enemy)

def main_place(hero):
    go_to = input("Where to? (bathroom/cafeteria/office/lockeroom)")
    if go_to == "bathroom":
        bathroom_scene(hero)
    if go_to == "cafeteria":
        cafeteria(hero)

def cafeteria(hero):
    time.sleep(1)
    print("""Coming from around the corner, you can smell the stench of processed
    food as the lunch ladies begin to cook for the day.  It's still pretty early""")
    time.sleep(1)
    print("""The tables and floors are spotless, not a tray in sight, there probably
    isn't much to see here.""")
    time.sleep(1)
    print("""However,""")
    time.sleep(1)
    print("""There is a distinct smell of cigarette smoke lingering from the cracked
    door to the outside on the other side of the cafeteria.  Someone is probably
    having a smoke break, but since you are bored, you decide to go outside.""")
    in_area = True
    while(in_area):
        print("""The lunch ladies are taking a smoke break with some of the
        'burnouts'.  There isn't much to talk about....""")
        init_fight(hero)
        # if password in hero.inventory:
        #     decision = input("What do you know?")
        #     if decision = hero.inventory: #the password
        #         # Give hero this item.
        #     else:
        #         print("Scram kid!")
        print("Don't tell anyone we're here!")
        print("You leave them and go back to the main hall")
        in_area = False
    main_place(hero)

def bathroom_scene(hero):
    time.sleep(1)
    print("""You've entered the bathroom.  Just a regular bathroom, but some of
    the 'bad kids' hangout here.  It smells like someone was smoking in here
    probably a couple of hours ago.""")
    time.sleep(1)

    in_area = True
    while(in_area):
        decision = input("What to do now? (wash hands/leave)")
        init_fight(hero)
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
            in_area= False

    main_place(hero)

import random
from fight_sequence import *
import time

def init_fight(hero):
    fight = random.random()
    if fight < .3:
        enemy = bestiary[str(random.choice(list(bestiary.items()))[0])]
        fight_seq(hero, enemy)
# def character_gen():


def intro(hero):
    print("""School sucks, but being a senior gives you some privileges above all
    of the other classes.  Plus, having a part time job has allowed you to pull out a
    small loan for a decent car.""")
    time.sleep(1)
    print("""Also, it's April and you've decided to skip the first two periods.
    Luckily today the school's administration is a bit relaxed today, which is
    a bit weird, but you quickly over look that fact anyways.""")
    time.sleep(1)
    print("""As you pass through the administrative offices, you overhear that the
    principal is gone, but don't hear the reason, and that someone is waiting in
    detention because of a drug accusation.""")
    time.sleep(1)
    print("""You realize that they're refering to one of your best friends, and you
    know for a fact that he doesn't do any drugs, so there has to be a way to find out
    what the accusations are, and if they're ungrounded, destroy the paperwork to save
    your friends reputation.""")
    time.sleep(1)
    print("""You make a left to enter the main hall around the corner...""")
    time.sleep(1)

def main_place(hero):
    go_to = input("Where to? (bathroom/cafeteria/office/lockeroom)")
    if go_to == "bathroom":
        bathroom_scene(hero)
    if go_to == "cafeteria":
        cafeteria(hero)
def office(hero):
    time.sleep(1)
    print("""""")
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

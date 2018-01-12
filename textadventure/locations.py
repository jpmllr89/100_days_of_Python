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
    print("""Welcome to the stereotypical watered-down zelda-esque adventure game with an RPG loop.  You just came out of the forest
    and have no idea who you are.  As you scout the land, the plain is pretty vast and empty, nothing but a sea
    of grass.""")
    time.sleep(1)
    print("""To the left you see a welcoming village, to the right you see a mountain surrounded by billowing dark clouds.""")
    time.sleep(1)

def plains(hero):
    print("You walk a little bit more out into this sea of grass....")
    time.sleep(1)
    go_to = input("Where to? (village/mountain)")
    if go_to == "village":
        village(hero)
    if go_to == "mountain":
        mountain(hero)

def village(hero):
    time.sleep(1)
    print("""You just entered through the town's gates.  Even though the village seemed pretty close,
    it took longer than realized to make to the village.  Because of that, you're a bit tired.""")
    time.sleep(1)
    print("""At the town square, you see a pavilion that hosts scraps of advertisements.
    Ever since the advent of this new thing called 'writing', a towncrier is no longer necessary.
    """)
    time.sleep(1)
    print("""To the left of the pavilion, there is an inn.  Looks like a great place for gossip and to rest.""")
    time.sleep(1)
    print("""To the right, there is a small market place.  You can hear vendors obnoxiously repeating what they have.""")
    if "letter" in hero.inventory:
        goto = input("Where would you like to go? (market/inn/plains/mountains)")
    else:
        goto = input("Where would you like to go? (market/inn/plains)")
        if goto =="market":
            marketplace(hero)
        if goto =="inn":
            inn(hero)

def marketplace(hero):
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

def scale_mountain(hero):
    print("""You have climbed almost to the top.  There is a flat area that leads to a cave,
    but you hesitate because you've been climbing pretty much all day.""")
    time.sleep(1)
    print("""You know the dragon is probably inside the cave and you have to slay it eventually
    but you're pretty tired.""")
    time.sleep(1)
    rest = input("""Did you remember to buy some potions to replenish your health? (y/n)""")
    if rest =="y":
        print("""Great, let's use them before the dragon attacks!""")
    else:
        print("""you fool!  The dragon sticks its head out, rips your intestines out because you were too tired.""")
def mountain(hero):
    print("""The trail increasingly becomes steeper and more winded by boulders.
    Straight ahead, you can see the mountain ominously reaches up into the clouds.""")
    time.sleep(1)
    print("""As you turn from another boulder, the trail leads to a guard
    protecting a gateway that leads into a canyon.  This is a totally original motif, ok?
    """)
    time.sleep(1)
    print("""The guard asks you to state your business.""")
    time.sleep(1)
    business = input("Request to go inside? (y/n)")
    if business=='y':
        if 'letter' in hero.inventory:
            scale_mountain(hero)

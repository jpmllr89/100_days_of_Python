import random
from player import *
from item_dictionary import items
from fight_sequence import *
import time

def init_fight(hero):
    fight = random.random()
    if fight < .3:
        enemy = bestiary[str(random.choice(list(bestiary.items()))[0])]
        fight_seq(hero, enemy)
# def character_gen():

def fight_dragon(hero):
    enemy = bestiary["Dragon"]
    fight_seq(hero, enemy)

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
    go_to = input("Where to? (village/mountain/venture)")
    if go_to == "village":
        init_fight(hero)
        village(hero)
    if go_to == "mountain":
        init_fight(hero)
        mountain(hero)
    if go_to =="venture":
        init_fight(hero)
        plains(hero)
    else:
        init_fight(hero)
        plains(hero)


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
    print("""People say it's not as busy as it usually is.  There are three stands
    open.  One in particular, that has an assortment of shiny swords and mysterious
    potions catches your eye.""")
    time.sleep(1)
    print("""You walk towards that one.""")
    in_area = True
    while(in_area):
        print("""Welcome to my store.  What would you like to buy?""")
        for key, value in items.items():
            print(value.name + " --- "+ str(value.buy)+" gold")
        selection = input("Type Selection here >>  ")
        if hero.pay(items[selection].buy)==True:
            hero.add_to_inventory(items[selection].name)
        again = input("""Anything else?""")
        if again == "n":
            go_back= input("Return to village? (y/n)")
            if go_back == "y":
                village(hero)

def inn(hero):
    time.sleep(1)
    print("""You step into a raucous tavern.  There are people drinking and talking in various
    places, some are sitting around the fire.""")
    time.sleep(1)
    print("""You don't really have much time, because you have to slay a dragon
    on top of the mountain.  You might as well stay here for a spell anyways
    since you don't know how to scale the mountain in the first place.""")
    time.sleep(1)
    print("""This place is teeming with gossip, so first thing first, go to the bartender
    and get a drink.""")
    atBar = True
    while(atBar):
        bar = input("The bartender asks you what you would like to do. (Sleep/Talk)")
        if bar =="Sleep":
            print("Have a good night!")
            time.sleep(1)
            hero.health = 25
            print("Your health is replenished!: "+ str(hero.health))
        elif "permit" in hero.inventory:
            print("The bartender reminds you to come back alive because he shouldn't give his brother's permit to anyone.")
        elif bar=="Talk":
            print("""You ask how to get inside the mountain's cave.  The bartender
            pauses, hesitates to disclose, but then spills all.""")
            time.sleep(1)
            print("""He explains that there is an imperial guard at the gate once you hike through
            the end of the quarry.  He will not let anyone through that doesn't have a permit.  Since
            your intentions are pure, however, he will give you his brother's permit, who also
            happens to be an adventurer like yourself.""")
            time.sleep(1)
            hero.add_to_inventory("permit")
            print("You received the permit from the bartender!")
            time.sleep(1)
            print("Now it's time to slaaaayy")
            village(hero)


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
        if "potion" in hero.inventory:
            hero.health += hero.inventory[hero.inventory.index("potion")]
    else:
        print("""you fool!  The dragon sticks its head out, rips your intestines out because you were too tired.""")


def mountain(hero):
    hero.list_inventory()
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
        if 'permit' in hero.inventory:
            scale_mountain(hero)

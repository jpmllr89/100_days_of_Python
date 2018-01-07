from fight_sequence import *
from player import *
from locations import *
hero = Hero("Jesse", 25, 25, 25)

def game_sequence(hero):
    enemy = bestiary[str(random.choice(list(bestiary.items()))[0])]
    bathroom_scene(hero)
    fight_seq(hero, enemy)
    ask = input("Play again? (y/n)")
    if ask == "y":
        game_sequence(hero)
    else:
        print(" bye!")

game_sequence(hero)

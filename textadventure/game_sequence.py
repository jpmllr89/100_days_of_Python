from fight_sequence import *
from player import *
from locations import *
from save_state import *
hero = Hero("Jesse", 25, 25, 25)

def game_sequence(hero):
    intro(hero)
    main_place(hero)

# game_sequence(hero)
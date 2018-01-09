from game_sequence import *


save_states = {
}

hero = Hero("Jesse", 25, 25, 25)
def delete():
    for key in save_states:
        print(save_states[key].name)
    print("Which one will you delete?")
    deletion = input("Enter Name here>>  ")
    for key in save_states:
        if key == deletion:
            del save_states[key]

def record_to_text(save_states):
    text='{ '
    path = "save.txt"
    saves = open(path, 'w')
    for key, value in save_states.items():
        text = text + str(key) + ':' + str(value) +', '
    text += '}'
    saves.write(text)
    saves.close()

def parse_text(save_states):
    path = "save.txt"
    saves= open(path, 'r')
    txt = saves.read()
    print(txt)


def save(hero):
    if len(save_states)<3:
        save_states.update({hero.name:[hero.name, hero.health, hero.strength, hero.gold]})
    else:
        print("You must delete another Entry")
# save(hero)
#
# record_to_text(save_states)
# parse_text(save_states)

#
# for key,value in save_states.items():
#     print(key, value)

# delete()

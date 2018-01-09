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

def save(hero):
    if len(save_states)<3:
        save_states.update({hero.name:hero})
        # print(save_states)
    else:
        print("You must delete another Entry")

save(hero)

for key in save_states:
    print(save_states[key].name)

# delete()

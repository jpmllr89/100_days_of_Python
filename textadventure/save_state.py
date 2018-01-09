from game_sequence import *
import csv

save_states = {
}

hero = Hero("Jesse", 25, 25, 25)
hero1= Hero("peter", 23,23,23)
def delete():
    for key in save_states:
        print(save_states[key].name)
    print("Which one will you delete?")
    deletion = input("Enter Name here>>  ")
    for key in save_states:
        if key == deletion:
            del save_states[key]

def record_to_text(save_states, path):
    with open(path, 'w') as csvfile:
        write = csv.writer(csvfile)
        for key, value in save_states.items():
            write.writerow([key, value])

def parse_text(save_states, path):
    with open(path, 'r') as csvfile:
        readcsv = csv.reader(csvfile, delimiter = ',')
        for row in readcsv:
            make_data = []

            save_states.update({ row[0] : row[1]})



def save(hero):
    if len(save_states)<3:
        save_states.update({hero.name:[hero.name, hero.health, hero.strength, hero.gold]})
    else:
        print("You must delete another Entry")
save(hero)
# print(save_states)
save(hero1)
# print(save_states)

record_to_text(save_states, 'save.csv')
parse_text(save_states, 'save.csv')

print(save_states)
# parse_text(save_states)

#
# for key,value in save_states.items():
#     print(key, value)

# delete()

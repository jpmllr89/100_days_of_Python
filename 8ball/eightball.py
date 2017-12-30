import random
import game_functions

def console():
    again = True
    while(again):
        request = input("Type question here and press Enter >>  ")
        print(request)
        game_functions.QUESTIONS.append(request)
        print('...')
        print('...')
        print('...')
        print('...')
        game_functions.eightball(game_functions.generateNum())

        print("Ask another or see previous questions?")
        game_functions.replay()



console()

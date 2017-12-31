import random

def randInt():
    return random.randint(0,2)

def game():
    gen = ''
    flag = True
    while(flag):
        gesture = input("Rock paper or scissors?")
        gesture = gesture.lower()
        bang = randInt()
        if bang == 0:
            gen = 'rock'
        elif bang == 1:
            gen = 'paper'
        elif bang == 2:
            gen = 'scissors'

        print(gen)

        if gesture == gen:
            print("DRAW!")
        elif gen == 'rock':
            if gesture == 'scissors':
                print('you lose!')
            else:
                print('you win!')
        elif gen == 'paper':
            if gesture == 'rock':
                print('you lose!')
            else:
                print('you win!')
        elif gen == 'scissors':
            if gesture == 'paper':
                print('you lose!')
            else:
                print('you win!')

        ask = input("Would you like to play again? (y/n)")
        if ask == 'y':
            flag = True
        else:
            flag = False

game()

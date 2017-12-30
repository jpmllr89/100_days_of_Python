import random

def numguess():
    RAND = random.randint(1,100)
    play = True
    gamecount = 0
    print("I'm thinking of a number between 1-100")
    while(play):
        number = int(input("Can you guess what it is?  "))
        gamecount +=1
        if gamecount > 10:
            print("you ran out of tries!")
            play = False
        elif number > RAND:
            print("Go lower!")
        elif number < RAND:
            print("Go Higher!")
        elif number==RAND:
            print("You got it!")
            play = False

def replay():
    sure = input("Would you like to play again?(y/n)  ")
    if sure =="y":
        numguess()
    elif sure =='n':
        print("bye!")

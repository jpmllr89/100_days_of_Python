import random

questions = []

def generateNum():
    num = random.randint(1, 8)
    return num

def eightball(ans):
    if ans == 1:
        print("You will have a better fortune")
    elif ans == 2:
        print("Yes")
    elif ans == 3:
        print("No")
    elif ans == 4:
        print("Lol maybe")
    elif ans == 5:
        print("HELL NO")
    elif ans == 6:
        print("Absolutely!")
    elif ans == 7:
        print("Nah")
    elif ans == 8:
        print("Ok.")

def console():
    again = True
    while(again):
        request = input("Type question here and press Enter >>  ")
        print(request)
        QUESTIONS.append(request)
        print('...')
        print('...')
        print('...')
        print('...')
        eightball(generateNum())

        print("Ask another or see previous questions?")


        quest = input("(Press 'n' to quit or q to see questions")
        if quest == "n":
            again = False
        elif quest =="q":
            for i in questions:
                print(i)
            again = False



console()

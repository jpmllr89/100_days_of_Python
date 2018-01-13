from tkinter import *
import math

class calculator():

    # below are definitions for starting up the number and operator buttons.
    # don't know enough to incorporate some for loop functionality into my init statements yet.
    # def startOperators(self, operatorpad):
    #     ops = ["*", "+", "-", "/"]
    #     i = 0
    #     operators = []
    #     for j in range(0,3):
    #         for k in range(0, len(ops)):
    #             operators.append(Button(operatorpad, text = str(ops[i])))
    #             operators[i].grid(row=j, column = k)
    #             i+=1

    def startNumbers(self, numpad):
        nums = [9,8,7,6,5,4,3,2,1,0]
        numbers = []
        i = 0
        for j in range(0,3):
            for k in range(0,3):
                numbers.append(Button(numpad, text=str(nums[i])))
                numbers[i].grid(row=j, column = k)
                i+=1
        Button(numpad, text=str(nums[9])).grid(row=4, column = 1, pady=5)
        Button(numpad, text=".").grid(row=4, column = 2, pady=5)
    def printer(self):
        print("pressed!")
    def __init__(self, app):
        app.title('Calculator')
        answer = Frame(app)
        answer.pack(side=TOP)

        self.entry = Entry(answer)
        self.entry.grid(row=0, column = 0, columnspan=6)
        numpad = Frame(app)
        numpad.pack(side=LEFT)
        self.startNumbers(numpad)
        # nothing sophisticated for the operators.
        operatorpad = Frame(app)
        operatorpad.pack(side=RIGHT)
        Button(operatorpad, text = '+', command = self.printer).grid(row = 0, column = 0, pady=1, padx = 2)
        Button(operatorpad, text = '-', command = self.printer).grid(row = 1, column = 0, pady=1, padx = 2)
        Button(operatorpad, text = '/', command = self.printer).grid(row = 2, column = 0, pady=1, padx = 2)
        Button(operatorpad, text = '*', command = self.printer).grid(row = 3, column = 0, pady=1, padx = 2)
        Button(operatorpad, text = '^', command = self.printer).grid(row = 0, column = 1, pady=1, padx = 2)
        Button(operatorpad, text = 'sqrt()', command = self.printer).grid(row = 1, column = 1, pady=1, padx = 2)
        Button(operatorpad, text = 'C', command = self.printer).grid(row = 2, column = 1, pady=1, padx = 2)
        Button(operatorpad, text = '=', command = self.printer).grid(row = 3, column = 1, pady=1, padx = 2)









# app=Tk()
# calc = calculator(app)
# app.mainloop()

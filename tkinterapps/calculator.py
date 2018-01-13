from tkinter import *


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
    def printer(self):
        print("pressed!")
    def __init__(self, app):
        app.title('Calculator')
        self.entry = Entry(app)
        numpad = Frame(app)
        numpad.pack(side=LEFT)
        # oppad = Frame(app)
        # oppad.pack(side = RIGHT)
        self.startNumbers(numpad)
        # self.startOperators(oppad)

        # For now I will have to add the buttons individually, since this is a bit new to me.
        # Button(numpad, text = '9', command = self.printer).grid(row = 0, column = 0, pady=5, padx = 5)
        # Button(numpad, text = '8', command = self.printer).grid(row = 0, column = 1, pady=5, padx = 5)
        # Button(numpad, text = '7', command = self.printer).grid(row = 0, column = 2, pady=5, padx = 5)
        # Button(numpad, text = '6', command = self.printer).grid(row = 1, column = 0, pady=5, padx = 5)
        # Button(numpad, text = '5', command = self.printer).grid(row = 1, column = 1, pady=5, padx = 5)
        # Button(numpad, text = '4', command = self.printer).grid(row = 1, column = 2, pady=5, padx = 5)
        # Button(numpad, text = '3', command = self.printer).grid(row = 2, column = 0, pady=5, padx = 5)
        # Button(numpad, text = '2', command = self.printer).grid(row = 2, column = 1, pady=5, padx = 5)
        # Button(numpad, text = '1', command = self.printer).grid(row = 2, column = 2, pady=5, padx = 5)
        # Button(numpad, text = '0', command = self.printer).grid(row = 3, column = 1, pady=5, padx = 5)
        # operatorpad = Frame(app)
        # operatorpad.pack(side=RIGHT)
        # Button(operatorpad, text = '+', command = self.printer).grid(row = 0, column = 0, pady=5, padx = 5)
        # Button(operatorpad, text = '-', command = self.printer).grid(row = 1, column = 0, pady=5, padx = 5)
        # Button(operatorpad, text = '/', command = self.printer).grid(row = 2, column = 0, pady=5, padx = 5)
        # Button(operatorpad, text = '*', command = self.printer).grid(row = 3, column = 0, pady=5, padx = 5)








# app=Tk()
# calc = calculator(app)
# app.mainloop()

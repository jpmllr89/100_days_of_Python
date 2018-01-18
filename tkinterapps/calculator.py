from tkinter import *
import math
import time
class calculator():

    def clear(self):
        box = self.entry.get()
        self.entry.delete(-1)

    def all_clear(self):
        box = self.entry.get()
        self.entry.delete(0,END)

    def evaluate(self):
        equation = self.entry.get()
        try:
            answer = eval(equation)
        except SyntaxError:
            self.entry.delete(0,END)
            time.sleep(1)
            self.entry.insert(END, "Check your equation!")
            time.sleep(1)
            self.entry.delete(0,END)

        else:
            self.entry.delete(0,END)
            self.entry.insert(END,answer)


    def startNumbers(self, numpad):
        nums = [9,8,7,6,5,4,3,2,1,0]
        numbers = []
        for i in range(0,10):
          numbers.append(Button(numpad, text=str(i), command = lambda num = i:self.insert_to_entry(num)))
        numbers[0].grid(row=3, column = 1)
        numbers[1].grid(row=2, column = 0)
        numbers[2].grid(row=2, column = 1)
        numbers[3].grid(row=2, column = 2)
        numbers[4].grid(row=1, column = 0)
        numbers[5].grid(row=1, column = 1)
        numbers[6].grid(row=1, column = 2)
        numbers[7].grid(row=0, column = 0)
        numbers[8].grid(row=0, column = 1)
        numbers[9].grid(row=0, column = 2)
        Button(numpad, text=".", command = lambda:self.insert_to_entry('.')).grid(row=3, column = 2)

    def start_operators(self, operatorpad):
        ops = ['+', '-', '/', '*']
        operators = []
        Button(operatorpad, text = '+', command = lambda:self.insert_to_entry('+')).grid(row = 0, column = 0)
        Button(operatorpad, text = '-', command = lambda:self.insert_to_entry('-')).grid(row = 1, column = 0)
        Button(operatorpad, text = '/', command = lambda:self.insert_to_entry('/')).grid(row = 2, column = 0)
        Button(operatorpad, text = '*', command = lambda:self.insert_to_entry('*')).grid(row = 0, column = 1)
        Button(operatorpad, text = '^2', command = lambda:self.power()).grid(row = 1, column = 1)
        Button(operatorpad, text = 'sqrt()', command = lambda:self.sqroot()).grid(row = 2, column = 1)
        Button(operatorpad, text = 'AC', command = lambda:self.all_clear()).grid(row= 1, column = 2)
        Button(operatorpad, text = 'C', command= lambda:self.clear()).grid(row = 2, column = 2,)
        Button(operatorpad, text = '=', command = lambda:self.evaluate()).grid(row = 3, column = 0)

    def sqroot(self):
        num = self.entry.get()
        sqroot = math.sqrt(float(num))
        self.entry.delete(0, END)
        self.entry.insert(END, sqroot)

    def power(self):
        num = self.entry.get()
        power = float(num)**2
        self.entry.delete(0, END)
        self.entry.insert(END, power)

    def insert_to_entry(self, arg):
        self.entry.insert(END, arg)

    def __init__(self, app):
        app.title('Calculator')
        # top frame to hold evaluation
        answer = Frame(app)
        answer.pack(side=TOP)
        # packs entry into top frame
        self.entry = Entry(answer)
        self.entry.grid(row=0, column = 0, columnspan=6)
        # creates the number pad
        numpad = Frame(app)
        numpad.pack(side=LEFT)
        self.startNumbers(numpad)
        # create operation pad
        operatorpad = Frame(app)
        operatorpad.pack(side=RIGHT)
        self.start_operators(operatorpad)








# app=Tk()
# calc = calculator(app)
# app.mainloop()

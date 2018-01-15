from tkinter import *
import math
import time
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
            self.entry.insert(END, "Check your equation!")
            time.sleep(1)
            self.entry.delete(0,END)
        else:
            print(answer)
            if len(self.memory)>0:
                self.memory.pop()
                self.entry.delete(0,END)
                self.entry.insert(END,answer)
                self.memory.append(answer)
                self.entry.delete(0)
            else:
                self.entry.delete(0,END)
                self.entry.insert(END,answer)
                self.memory.append(answer)
                print(self.memory)

    def startNumbers(self, numpad):
        # nums = [9,8,7,6,5,4,3,2,1,0]
        # numbers = []
        # i = 0
        # for j in range(0,3):
        #     for k in range(0,3):
        #         numbers.append(Button(numpad, text=str(nums[i]), command = lambda:self.insert_to_entry(nums[i])))
        #         numbers[i].grid(row=j, column = k)
        #         i+=1
        Button(numpad, text=str(0), command = lambda:self.insert_to_entry(0)).grid(row=3, column = 1)
        Button(numpad, text=str(1), command = lambda:self.insert_to_entry(1)).grid(row=2, column = 0)
        Button(numpad, text=str(2), command = lambda:self.insert_to_entry(2)).grid(row=2, column = 1)
        Button(numpad, text=str(3), command = lambda:self.insert_to_entry(3)).grid(row=2, column = 2)
        Button(numpad, text=str(4), command = lambda:self.insert_to_entry(4)).grid(row=1, column = 0)
        Button(numpad, text=str(5), command = lambda:self.insert_to_entry(5)).grid(row=1, column = 1)
        Button(numpad, text=str(6), command = lambda:self.insert_to_entry(6)).grid(row=1, column = 2)
        Button(numpad, text=str(7), command = lambda:self.insert_to_entry(7)).grid(row=0, column = 0)
        Button(numpad, text=str(8), command = lambda:self.insert_to_entry(8)).grid(row=0, column = 1)
        Button(numpad, text=str(9), command = lambda:self.insert_to_entry(9)).grid(row=0, column = 2)
        Button(numpad, text=".", command = lambda:self.insert_to_entry('.')).grid(row=3, column = 2)

    def start_operators(self, operatorpad):
        Button(operatorpad, text = '+', command = lambda:self.insert_op_to_entry('+')).grid(row = 0, column = 0, pady=1, columnspan=1)
        Button(operatorpad, text = '-', command = lambda:self.insert_op_to_entry('-')).grid(row = 1, column = 0, pady=1, columnspan=1)
        Button(operatorpad, text = '/', command = lambda:self.insert_op_to_entry('/')).grid(row = 2, column = 0, pady=1, columnspan=1)
        Button(operatorpad, text = '*', command = lambda:self.insert_op_to_entry('*')).grid(row = 0, column = 1, pady=1, columnspan=1)
        Button(operatorpad, text = '^2', command = lambda:self.power()).grid(row = 1, column = 1, pady=1, columnspan=1)
        Button(operatorpad, text = 'sqrt()', command = lambda:self.sqroot()).grid(row = 2, column = 1, pady=1, columnspan=1)
        Button(operatorpad, text = 'AC', command = lambda:self.all_clear()).grid(row= 1, column = 2, columnspan=1)
        Button(operatorpad, text = 'C', command= lambda:self.clear()).grid(row = 2, column = 2, pady=1, columnspan=1)
        Button(operatorpad, text = '=', command = lambda:self.evaluate()).grid(row = 3, column = 0, columnspan=3)

    # def memory(self):
    #     try:
    #         self.entry.delete(0,End)
    #         self.entry.insert(END, self.memory.pop())
    #     except SyntaxError:
    #         self.entry.delete(0,END)
    #         self.entry.insert(END, "Nothing in memory!")

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

    def insert_op_to_entry(self, arg):
        self.entry.insert(END,arg)
    def insert_to_entry(self, arg):
        print(self.entry.get()[:-1])
        if self.entry.get()[:-1] in ['+', '-', '/', '*']:
            self.entry.insert(END,arg)
        elif len(self.memory)>0:
            self.memory.pop()
            self.entry.delete(0,END)
            self.entry.insert(END, arg)
        else:
            self.entry.insert(END,arg)

    def __init__(self, app):
        app.title('Calculator')
        answer = Frame(app)
        answer.pack(side=TOP)
        self.memory = []
        # self.calc_memory = []
        self.entry = Entry(answer)
        self.entry.grid(row=0, column = 0, columnspan=6)
        # self.entry.focus_set()
        numpad = Frame(app)
        numpad.pack(side=LEFT)
        self.startNumbers(numpad)
        operatorpad = Frame(app)
        operatorpad.pack(side=RIGHT)
        self.start_operators(operatorpad)








# app=Tk()
# calc = calculator(app)
# app.mainloop()

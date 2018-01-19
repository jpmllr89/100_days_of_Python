from tkinter import *
import math
import time


class Calculator():
    def percent(self):
        num =self.entry.get()
        percent = float(num)/100
        self.entry.delete(0,END)
        self.entry.insert(END,percent)

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


    # def startNumbers(self, numpad):


    def generate_operatorpad(self, app):
        # commenting below two lines because for some reason, entering them like
        # the numbers function above does not work.
        # ops = ['+', '-', '/', '*']
        # operators = []
        operatorpad = Frame(app)
        operatorpad.pack(side=RIGHT)
        Button(operatorpad, width=3, text = '+', command = lambda:self.insert_to_entry('+')).grid(row = 0, column = 0)
        Button(operatorpad, width=3, text = '-', command = lambda:self.insert_to_entry('-')).grid(row = 1, column = 0)
        Button(operatorpad, width=3, text = '/', command = lambda:self.insert_to_entry('/')).grid(row = 2, column = 0)
        Button(operatorpad, width=3, text = '*', command = lambda:self.insert_to_entry('*')).grid(row = 0, column = 1)
        Button(operatorpad, width=3, text = '^2', command = lambda:self.power()).grid(row = 1, column = 1)
        Button(operatorpad, width=3, text = 'sqrt()', command = lambda:self.sqroot()).grid(row = 2, column = 1)
        Button(operatorpad, width=3, text = '%', command = lambda:self.percent()).grid(row = 0, column = 2)
        Button(operatorpad, width=3, text = 'AC', command = lambda:self.all_clear()).grid(row= 1, column = 2)
        Button(operatorpad, width=3, text = 'C', command= lambda:self.clear()).grid(row = 2, column = 2,)
        Button(operatorpad, width=3, text = '=', command = lambda:self.evaluate()).grid(row = 3, column = 0, columnspan = 3)


    def generate_numpad(self, app):
        numpad = Frame(app)
        numpad.configure(bg = "#222222")
        numpad.pack(side=LEFT)
        nums = [9,8,7,6,5,4,3,2,1,0]
        numbers = []
        for i in range(0,10):
          numbers.append(Button(numpad, fg = "#222222", width = 3, overrelief = SUNKEN, text=str(i), command = lambda num = i:self.insert_to_entry(num)))
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


    def __init__(self, app):
        app.title('Calculator')
        # top frame to hold evaluation
        answer = Frame(app)
        answer.pack(side=TOP)
        # packs entry into top frame
        self.entry = Entry(answer)
        self.entry.pack(fill=X, expand = True)
        # creates the number pad
        self.generate_numpad(app)
        # create operation pad
        self.generate_operatorpad(app)


def main():
    app=Tk()
    app.configure(background = "#222222")
    calc = Calculator(app)
    app.mainloop()

if __name__ == "__main__":
    main()

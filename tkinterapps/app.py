# from tkinter import *
from calculator import *


which_app = input("Which app? (calculator)>>")
if which_app =="calculator":
    app = Tk()
    calc = calculator(app)
app.mainloop()

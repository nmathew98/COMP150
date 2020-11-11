from tkinter import *
from tkinter.messagebox import *

class HelloWorld:
    def __init__(self, parent):
        showinfo(message="Hi there")
        
root = Tk()
app = HelloWorld(root)
root.mainloop()
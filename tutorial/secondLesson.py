from tkinter import *
# positioning


# first widget that always have to be. Creates root window
root = Tk()

# Label ?? Label widget . Creating things
myLabel1 = Label(root,text='Hello World')
myLabel2 = Label(root,text='My name is x y ')
myLabel3 = Label(root,text='My name is z y ')

#  Labels are relative to each other. Putting the onto screena
myLabel1.grid(row = 0 , column = 0)
myLabel2.grid(row = 1 , column = 5)
myLabel3.grid(row = 2 , column = 2)


root.mainloop()

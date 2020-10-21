from tkinter import *
# input


# first widget that always have to be. Creates root window
root = Tk()

e = Entry(root,width =50,bg='green')
#attributes
#border width
e.pack()
#default text in input
e.insert(0,"Enter your name")

#get what is in input
e.get()


#After clicking button , text in input is displayed
def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text =hello)
    myLabel.pack()

#button() widget . Can contain text or image.
myButton = Button(root, text= 'submit', command = myClick, )



myButton.pack()


#infinite loop used to run application, wait for an event to occur and process the event as long as the window is not closed
root.mainloop()

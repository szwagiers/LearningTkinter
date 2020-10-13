from tkinter import *
# buttons


# first widget that always have to be. Creates root window
root = Tk()

def myClick():
    myLabel = Label(root, text ='Does it work ?')
    myLabel.pack()


myButton = Button(root, text= 'click me', command = myClick, fg='blue',bg='red')

# states of buttons
# DISABLED

#attributes
# padding padx or pady
# command, dont add () at the end
# fg - color of font; can use hex
# bg - background color


myButton.pack()



root.mainloop()

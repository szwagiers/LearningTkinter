from tkinter import *
from PIL import ImageTk,Image

# radio buttons

root = Tk()
root.title('Lesson12')
root.iconbitmap('D:/ikony/book.ico')

# defining variable as integer, aslo can pass String as StrVar()
#r = IntVar()

#r.get()
#r.set(2)

MODES = [('pepperoni','pepperoni')
,('cheese','cheese')
,('mushroom','mushroom')
,('onion','onion')
]

pizza = StringVar()
pizza.set('pepperoni')

for text,mode in MODES:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)

def show_value(value):
    # show value from Radiobutton
    myLabel = Label(root,text = value)
    myLabel.pack()


# adding radio button widger
# adding variable with value 1 as option 1
# Radiobutton(root, text='Option 1',variable=r,value = 1,command=lambda:show_value(r.get())).pack()
# Radiobutton(root, text='Option 2',variable=r,value = 2,command=lambda:show_value(r.get())).pack()

# show value from Radiobutton
# myLabel = Label(root,text = r.get())
# myLabel.pack()

myButton = Button(root, text='x',command=lambda:show_value(pizza.get())).pack()


mainloop()

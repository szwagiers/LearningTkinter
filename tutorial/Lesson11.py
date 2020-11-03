from tkinter import *
from PIL import ImageTk,ImageTk

#adding frames

root=Tk()
root.title('Lesson11')

root.iconbitmap('D:/ikony/book.ico')

#creating a frame, changing internal padding
frame = LabelFrame(root, text ='This is my frame', padx =10 , pady=10)

#changing external padding
frame.pack(padx=25,pady=25)

#IMPORTANT - inside frame one can add grid. Normally it is not allowed to use pack and grid simultaneously.
#place button inside frame not root
b = Button(frame, text='Button')
b2 = Button(frame, text='Button2')
b.grid(row=0,column=0)
b2.grid(row=1,column=2)




root.mainloop()

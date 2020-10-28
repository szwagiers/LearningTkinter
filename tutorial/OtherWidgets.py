from tkinter import *
root=Tk()


# text widget allows to put multiline text
t=Text()
#order of widgets is important. Widgets will show up in the same order as they are initialized with pack() method
#e.pack()
t.pack()

#infinite loop used to run application, wait for an event to occur and process the event as long as the window is not closed
root.mainloop()

#cannot mix grid and pack in master window.
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

myButton.pack()

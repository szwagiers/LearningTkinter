from tkinter import *
#icons, images, exit buttons

# tkinter have built-in system for images but only gif and pgm/ppm
# to open and display other formats like Jpg or png we need ImageTk and Image classes from PIL(photo imagining library)
# pip install Pillow in console
from PIL import ImageTk,Image

# Top level widget which is the main window of an application.
root = Tk()
# adds title of the application
root.title('Lesson 9')
# puts selected icon in top left corner of window. NOTE : If file is in the same folder as the program, there is no need to put full path to the file.
root.iconbitmap('D:/ikony/book.ico')

#putting images nedd 3 steps:
#1.define the image
my_img = ImageTk.PhotoImage(Image.open('D:/ikony/accept.png'))
#2.put image in other elements
my_label = Label(image = my_img)
#3.put these elements on screen
my_label.pack()


quit_button = Button(root, text='Exit',command = root.quit)

quit_button.pack()


#infinite loop used to run application, wait for an event to occur and process the event as long as the window is not closed
root.mainloop()

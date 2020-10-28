from tkinter import *
#image viewing app

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


my_img1 = ImageTk.PhotoImage(Image.open('D:/ikony/accept.png'))
my_img2 = ImageTk.PhotoImage(Image.open('D:/ikony/dollar.png'))
my_img3 = ImageTk.PhotoImage(Image.open('D:/ikony/industry.png'))
my_img4 = ImageTk.PhotoImage(Image.open('D:/ikony/mouse.png'))
my_img5 = ImageTk.PhotoImage(Image.open('D:/ikony/power-button.png'))
my_img6 = ImageTk.PhotoImage(Image.open('D:/ikony/alarm.png'))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5,my_img6]



my_label = Label(image = my_img1)
my_label.grid(row =0, column=0, columnspan =3)

def forward(img_num):
    global my_label,button_forward,button_back
    #make widget disappear from screen. It still exists, it just isn't visible.
    my_label.grid_forget()
    # we substract 1 because we are working on list index. If we pass 2 in function it will get image with index number 1
    my_label = Label(image=image_list[img_num-1])
    button_forward = Button(root,text=">>",command=lambda:forward(img_num+1))
    button_back = Button(root,text="<<",command=lambda:back(img_num-1))

    if img_num == 6:
        button_forward = Button(root, text='>>',state= DISABLED)

    my_label.grid(row =0, column=0, columnspan =3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)


def back(img_num):
    global my_label,button_forward,button_back
    my_label.grid_forget()

    my_label = Label(image=image_list[img_num-1])
    button_forward = Button(root,text=">>",command=lambda:forward(img_num+1))
    button_back = Button(root,text="<<",command=lambda:back(img_num-1))

    if img_num == 1:
        button_back = Button(root, text='<<',state= DISABLED)

    my_label.grid(row =0, column=0, columnspan =3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

button_back = Button(root,text="<<",command=lambda:back)
button_exit = Button(root,text="exit",command =root.quit)
#we want to pass 2 in button_forward because we are currently on image '1' and with pressing the button,we want to jump to image '2'
button_forward = Button(root,text=">>",command=lambda:forward(2))


button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)



#infinite loop used to run application, wait for an event to occur and process the event as long as the window is not closed
root.mainloop()

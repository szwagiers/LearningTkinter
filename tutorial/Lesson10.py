from tkinter import *

from PIL import ImageTk,Image

root = Tk()


root.title('Lesson10')


root.iconbitmap('D:/ikony/book.ico')

my_img1 = ImageTk.PhotoImage(Image.open('D:/ikony/accept.png'))
my_img2 = ImageTk.PhotoImage(Image.open('D:/ikony/dollar.png'))
my_img3 = ImageTk.PhotoImage(Image.open('D:/ikony/industry.png'))
my_img4 = ImageTk.PhotoImage(Image.open('D:/ikony/mouse.png'))
my_img5 = ImageTk.PhotoImage(Image.open('D:/ikony/power-button.png'))
my_img6 = ImageTk.PhotoImage(Image.open('D:/ikony/alarm.png'))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5,my_img6]

status = Label(root,text='Image 1 of ' + str(len(image_list)),bd = 1,relief=SUNKEN)
#can add anchor parameter


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
    #update status bar

    status = Label(root,text='Image '+ str(img_num) + ' of ' + str(len(image_list)),bd = 1,relief=SUNKEN)
    status.grid(row=2, column=1, sticky=W+E)


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
    #update status bar
    status = Label(root,text='Image '+ str(img_num) + ' of ' + str(len(image_list)),bd = 1,relief=SUNKEN)
    status.grid(row=2, column=1, sticky=W+E)

button_back = Button(root,text="<<",command=lambda:back)
button_exit = Button(root,text="exit",command =root.quit)
#we want to pass 2 in button_forward because we are currently on image '1' and with pressing the button,we want to jump to image '2'
button_forward = Button(root,text=">>",command=lambda:forward(2))


button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)
status.grid(row=2, column=1, sticky=W+E)


#infinite loop used to run application, wait for an event to occur and process the event as long as the window is not closed
root.mainloop()

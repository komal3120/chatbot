from tkinter import *

my_screen = Tk()
my_screen.configure(background='blue')
my_screen.title("Chatbot")

head = Label(my_screen,font=('arial',48,'bold'),text="                          Talk to chatterbot!!                            ",fg="black",bg="yellow")
head.pack(side=TOP)

left_side = Frame(my_screen,width=700,height=900,relief=SUNKEN,bg="black")
left_side.pack(side=LEFT)

my_screen.mainloop()

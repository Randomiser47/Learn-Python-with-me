from tkinter import *
window = Tk()
window.title("First Gui Program")
window.minsize(width=500,height=300)

#label
label = Label(text= "I AM A LABEL", font =("Arial",24,"bold"))
label.pack()


label.config(text="New TEeext")

#button
label.config(text="Button got clicked")

def button_click():
    wow = input.get()
    print(wow)
    label.config(text=wow)

button = Button(text="click me", command=button_click)
button.pack()



#entry component 
input = Entry(width=10)
input.pack()









window.mainloop()
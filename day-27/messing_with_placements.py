from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Placements")
window.minsize(width=500, height=500)
window.config(padx=10,pady=10) # This adds paddings on all the elements

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.grid(row=0,column=0)
label.config(padx=10,pady=10) # This adds paddings on only this element

#button
button = Button(text="Click Me")
button.grid(row=1,column=1)
#Spinbox
#new button
button = Button(text="New button")
button.grid(row=0,column=2)
#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
entry.grid(row=2,column=3)

window.mainloop()
from tkinter import *


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200,height=100)
window.config(pady=10,padx=10)


#Entry for Miles
entry = Entry(width=10)
entry.grid(row=0,column=1)

#Label for miles
label_miles = Label(text="Miles")
label_miles.grid(row=0,column=2)


#Label for is equal to
label_equal = Label(text="is equal to")
label_equal.grid(row=1,column=0)

#output into Kilometers
label_output = Label(text="0")
label_output.grid(row=1,column=1)

#Label for Kilometers
label_km = Label(text="Km")
label_km.grid(row=1,column=2)

#function for conversion
def mile_to_km():
    miles = float(entry.get())
    kilometers = miles * 1.609344
    label_output.config(text = kilometers)

#Button for calculate
button = Button(text="Calculate",command=mile_to_km)
button.grid(row=2,column=1)

window.mainloop()
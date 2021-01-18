from tkinter import *

window = Tk()
window.title('Mile to Km converter')
window.minsize(width=175,height=90)
window.config(padx=25,pady=10)

# Miles Input
miles_input = Entry(width=5)
miles_input.grid(column=1,row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2,row=0)

# Converted Section
equalTo_label = Label(text='is equal to ')
equalTo_label.grid(column=0,row=1)

equalTo_variable = Label(text='0')
equalTo_variable.grid(column=1,row=1)

equalTo_km = Label(text='Km')
equalTo_km.grid(column=2,row=1)

# Button
def button_clicked():
    miles = float(miles_input.get())
    km = miles * 1.609
    equalTo_variable['text'] = f'{km}'

button = Button(text='calculate', command=button_clicked)
button.grid(column=1,row=2)

window.mainloop()
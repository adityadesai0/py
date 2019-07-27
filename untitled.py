from tkinter import *
from tkinter.ttk import *
#window start
window = Tk()
#Title
window.title("GUI!")
#Window size
window.geometry('350x200')
#Body
#combobox/dropdown
combo = Combobox(window)
combo['values']=(1,2,3,4,5,"Text")
#label
lbl = Label(window, text="Hello, World!")#,font=("Arial Bold", 50))
#Alignment
lbl.grid(column=0, row=0)
#input
txt = Entry(window,width=10)#,state="disabled")
txt.grid(column=1, row=0)
#button click definition
def clicked():
    lbl.configure(text="Button was clicked!")
#button
btn = Button(window, text="Click Me", bg="orange", fg="red", command=clicked)
btn.grid(column=2, row=0)
#window end
window.mainloop()

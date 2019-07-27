from tkinter import *

# Start Window 1
window = Tk()
# Set title
window.title("Movie Booking")
# Window Size
window.geometry("200x200") # WidthxHeight

# Body

# Username Title
lb1 = Label(window, text="Username:")
lb1.grid(column = 0, row = 0)
# Username Input
user = Entry(window, width = 10)
user.grid(column = 0, row = 1)

# Password Title
lb2 = Label(window, text="Password:")
lb2.grid(column = 0, row = 2)
# Password Input
pasw = Entry(window, width = 10)
pasw.grid(column = 0, row = 3)

# Submit Button Definition/Command
def subm():
    booking()
    return

# Submit Button
submit = Button(window, text="Submit", command = subm)
submit.grid(column = 0, row = 4)

# Window 1 End
window.mainloop()


# Booking Function
def booking():
    return 0


# Window 2 Start
#window2 = Tk()


# Window 2 End

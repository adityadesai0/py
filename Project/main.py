from tkinter import *

user = "name"

# Booking Function
def booking():
    tic = open("ticket.txt", "w+") # Creating file "ticket.txt" in same dir and opening it in write mode.
    tic.write(user)
    tic = open("ticket.txt", "r")
    ticket = tic.read()
    print(ticket)
    tic.close()


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
user = str(user)
if user == "name":
    return 1
elif:
    return -1

# Password Title
lb2 = Label(window, text="Password:")
lb2.grid(column = 0, row = 2)
# Password Input
pasw = Entry(window, width = 10)
pasw.grid(column = 0, row = 3)

# Submit Button Definition/Command
def subm():
    booking()
    win1_close()

# Submit Button
submit = Button(window, text="Submit", command = subm)
submit.grid(column = 0, row = 4)

# Window 1 End
def win1_close():
    window.mainloop()



# Window 2 Start
window2 = Tk()
window2.title("Welcome!")
window2.geometry("500x500")
# Window 2 End
window2.mainloop()

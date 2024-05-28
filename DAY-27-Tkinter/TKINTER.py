from tkinter import *

def button_clicked():
    print("i got clicked")
    new_text = input.get()
    # To change the label to word which we write in box
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# To add space around the edges of the program
window.config(padx=20, pady=20)

# CREATE LABEL
my_label = Label(text="I am a Label", font=("Arial", 24, "italic"))
my_label.config(text="New Text")
# my_label.pack(side="left")  # For printing label on left
# my_label.pack()  # For printing label
# my_label.place(x=0, y=0)  # For placing label
my_label.grid(column=0, row=0)


button = Button(text="Click Me", command=button_clicked)
# Above we removed parenthesis from button clicked because it takes name of function and does
# not actually call it...
# button.pack()
button.grid(column=2, row=2)


# ENTRY
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=3)















window.mainloop()





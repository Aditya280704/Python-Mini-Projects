from tkinter import *
from tkinter import messagebox
import random
import pyperclip



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Using list comprehension
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers)for _ in range(nr_numbers)]
    password_list = password_symbol+password_numbers+password_letters

    random.shuffle(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    # or second way
    password = "".join(password_list)

    # print(f"Your password is: {password}")

    password_entry.insert(0, password)
    # To copy password in clipboard
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Pls dont leave field empty...")
    else:
        # MODULE FROM TKINTER:-
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail:{email}\npassword:{password}\n Is it ok to save?")
        if is_ok:
            # Using with we do not have to write file close command in end
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} || {email} || {password}\n")






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100,image=password_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)


email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)


password_label = Label(text="Password:")
password_label.grid(column=0, row=3)



# Entries

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)
# Automatically places the cursor in the website box
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2)
email_entry.insert(0, "aj8364524@gmail.com")
# If insert at the end then instead of 0 use END
# email_entry.insert(END, "aj8364524@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)







window.mainloop()















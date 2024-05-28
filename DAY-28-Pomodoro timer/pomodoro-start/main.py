from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # Returns largest whole no less than no, eg 4.8 so returns 4:-
    count_min = math.floor(count/60)
    count_sec = count % 60
    # Dynamic typing:-
    if count_sec == 0:
        count_sec = "00"
    # If we had a normal label then its text can easily be changed by using text.config(text = " ")
    # But for canvas its used like below:-
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # print(count)
    if count > 0:
        window.after(1000, count_down, count-1)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Execute a command after time delay.
# Just like time.sleep() in time module.
# window.after(1000, )


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50,))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
# Creating an image in canvas half in size of canvas
canvas.create_image(100, 112, image=tomato_img)
# Creating a text in canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="START", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="RESET")
reset_button.grid(column=2, row=2)

check_mark = Label(text="✔", fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row= 3)







window.mainloop()


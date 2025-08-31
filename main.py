from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
BLUE="#001BB7"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timmer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_count, text="00:00")
    label_text.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timmer():
    global reps
    reps += 1 
    
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    count_down(work_sec)
    if reps%8==0:
        count_down(long_break_sec)
        label_text.config(text="Long Break", fg=YELLOW)
    elif reps%2 == 0:
        count_down(short_break_sec)
        label_text.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        label_text.config(text="Work", fg=BLUE)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minute = math.floor(count/60)
    second = count%60
    if second < 0:
        second = (f"0{second}")

    canvas.itemconfig(timer_count, text=f"{minute}:{second}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timmer()
        marks = ""
        work_expression = math.floor(reps/2)
        for _ in range(work_expression):
            marks += "✔"
            check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=GREEN)
canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")

canvas.create_image(100,112,image=tomato_image)
timer_count = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)


label_text = Label(text="TIMER", font=(FONT_NAME, 25, "bold"), fg=BLUE, bg=GREEN)
label_text.grid(column=1, row=0)

check_mark = Label(text="", fg=BLUE, bg=GREEN)
check_mark.grid(column=1,row=3)

start_button = Button(text="Start", command=start_timmer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", command=reset_timmer)
reset_button.grid(column=2,row=2)

window.mainloop()
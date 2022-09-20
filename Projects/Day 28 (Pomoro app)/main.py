from tkinter import *
# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None

# FUNCTIONS


def restart_timer():
    # stopping timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    # resetting reps
    global reps
    reps = 0
    # resetting timer laber
    timer_label.config(text="POMODORO TIMER")
    # resetting checkmarks
    checkmark_label.config(text="")


def timer_controller():
    """This function controls which repetition the timer is on
    Depending on the repetition, it could be a work timer, a short break timer or a long break timer
    It does this by changing the global variable reps"""
    global reps
    reps += 1

    # long break
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        # changes timer label
        timer_label.config(text="LONG BREAK", foreground=RED)
    # short break
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        # changes timer label
        timer_label.config(text="SHORT BREAK", foreground=PINK)
        window.attributes('-topmost', 1)
    # work timer
    else:
        count_down(WORK_MIN)
        # changes timer label
        timer_label.config(text="WORKING SESSION", foreground=GREEN)


def count_down(count):
    """This functions receives a number os seconds, and counts down from it, updating the UI text
    If the count gets to 0, it calls timer_controller() to start the next session"""
    canvas.itemconfig(timer_text, text=timer_converter(count))
    if count > 0:
        global timer
        timer = window.after(100, count_down, count-1)
    else:
        # starting next timer
        timer_controller()
        # controlling checkmarks
        checkmarks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            checkmarks += "✔️"
        checkmark_label.config(text=checkmarks)


def timer_converter(time):
    """This function receives a number of seconds and converts it to a string showing minutes and seconds"""
    minutes = time // 60
    seconds = time % 60
    return f"{minutes:02d}:{seconds:02d}"


# ---------------------------- UI SETUP ------------------------------- #
# window setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# canvas
# add img
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
# add text
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# add to window
canvas.grid(column=2, row=2)

# TIMER text
timer_label = Label(text="POMODORO TIMER", font=(FONT_NAME, 24, "bold"), foreground=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)

# Start and Reset buttons
# start
start = Button(text="Start", highlightthickness=0, command=timer_controller)
start.grid(column=1, row=3)
# reset
start = Button(text="Reset", highlightthickness=0, command=restart_timer)
start.grid(column=3, row=3)

# Timer's Green Checkmark Counter
checkmark_label = Label(text="", font=(FONT_NAME, 12), foreground=GREEN, bg=YELLOW)
checkmark_label.grid(column=2, row=4)

# mainloop
window.mainloop()

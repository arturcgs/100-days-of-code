import tkinter as tk
from random import choice

END = "end"


def start_test():
    # create test screen
    test_screen = tk.Toplevel()
    test_screen.title("Test")
    test_screen.geometry("500x500")

    # choose random phrase
    with open('test_phrases.txt') as f:
        phrases = [line.rstrip('\n') for line in f]
    test_text_raw = choice(phrases)

    # widgets
    # test text
    test_text = add_break_line_to_text(test_text_raw)
    test_text_label = tk.Label(test_screen, text=test_text, font=("Arial", 24, "bold"), pady=20)
    test_text_label.pack()

    # type test
    type_test = tk.Text(test_screen, height=5, width=50)
    type_test.focus()
    type_test.pack()

    # finish test
    test_screen.after(
        20000,
        lambda: finish_test(screen=test_screen, test_text=test_text_raw.lower(), typed_text=type_test.get("1.0", END).lower())
    )


def finish_test(screen: tk.Toplevel, test_text: str, typed_text: str):
    wpm, accuracy = calculate_wpm(test_text, typed_text)
    wpm_value["text"] = f"{wpm:.2f}"
    accuracy_value["text"] = f"{accuracy:.2f}%"
    screen.destroy()


def calculate_wpm(test_text: str, typed_text: str):
    # separate words
    test_text_words = test_text.split()
    typed_text_words = typed_text.split()

    # select smallest list
    smallest_text = min(test_text_words, typed_text_words, key=len)

    # count correct chars
    correct_chars = 0
    total_chars = 0
    for test_word, typed_word in zip(test_text_words, typed_text_words):
        total_chars += len(typed_word)
        for test_letter, typed_letter in zip(test_word, typed_word):
            if test_letter == typed_letter:
                correct_chars += 1
    incorrect_chars = total_chars - correct_chars

    # calculate parameters
    gross_wpm = correct_chars / 5 * 3
    net_wpm = gross_wpm - (incorrect_chars * 3)
    if net_wpm < 0:
        net_wpm = 0
    accuracy = correct_chars / total_chars * 100

    return net_wpm, accuracy


def add_break_line_to_text(text):
    words = text.split()
    chars = 0
    text_with_line_breaks = ""

    for word in words:
        chars += len(word)
        if chars > 20:
            text_with_line_breaks += "\n"
            chars = 0

        text_with_line_breaks += word
        text_with_line_breaks += " "

    return text_with_line_breaks


# creating main page
main_page = tk.Tk()
main_page.title("Speed Typing Tester")
main_page.geometry("750x400")

#  main page widgets
# title
title_label = tk.Label(text="Welcome to the Speed Typing Tester", font=("Arial", 40, "bold"), pady=20)
title_label.grid(row=0, column=0, columnspan=2)

# instructions
instructions_label = tk.Label(text='Click "Start test" to take your test', font=("Arial", 26, "bold"), pady=20)
instructions_label.grid(row=1, column=0, columnspan=2)

# Current Score
current_score_label = tk.Label(text="Score:", font=("Arial", 16, "bold"), pady=20)
current_score_label.grid(row=2, column=0, columnspan=2)

wpm_label = tk.Label(text="Word Per Minute (WPM): ", font=("Arial", 16, "bold"))
wpm_label.grid(row=3, column=0)

wpm_value = tk.Label(text="", font=("Arial", 16, "bold"))
wpm_value.grid(row=3, column=1)

accuracy_label = tk.Label(text="Accuracy: ", font=("Arial", 16, "bold"))
accuracy_label.grid(row=4, column=0)

accuracy_value = tk.Label(text="", font=("Arial", 16, "bold"))
accuracy_value.grid(row=4, column=1)

# Start Button
start_button = tk.Button(text="Start test", command=start_test)
start_button.grid(row=5, column=0, columnspan=2)




main_page.mainloop()
import tkinter as tk


def button_click():
    mile = float(entry.get())
    calculated_km['text'] = f"{mile * 1.60934:.2f}"


# create window
window = tk.Tk()
window.title("Miles to Km converter")
window.config(padx=20, pady=20)

# creating labels
# miles
miles_label = tk.Label(text="Miles")
miles_label.grid(column=3, row=1)
# km
km_label = tk.Label(text="Km")
km_label.grid(column=3, row=2)
# is equal to
is_equal_to_label = tk.Label(text="is equal to")
is_equal_to_label.grid(column=1, row=2)
# calculated_km
calculated_km = tk.Label(text="0")
calculated_km.grid(column=2, row=2)

# creating entry
entry = tk.Entry(width=10)
entry.insert(0, string="0")
entry.grid(column=2, row=1)

# creating button
button = tk.Button(text="Calculate", command=button_click)
button.grid(column=2, row=3)

# mainloop
window.mainloop()

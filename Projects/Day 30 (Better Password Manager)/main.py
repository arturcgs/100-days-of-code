from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def password_generator():
    """This function generates a random password and puts it in the password entry"""
    # clearing the entry
    password_entry.delete(0, END)
    # password length
    length = 20
    # characters dict
    characters = {"letters": ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                              's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                              'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
                  "symbols": ["!", "@", "#", "$", "%", "&", "*", "(", ")", "|", "[", "]", "{", "}", ":", ",", ".", "<",
                              ">", ";", "?", "/", "+"],
                  "numbers": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]}

    # how many letters, symbols and numbers the password will have, chosen randomly
    num_letters = random.randint(1, length-1)
    num_symbols = random.randint(1, (length - num_letters))
    num_numbers = length - num_symbols - num_letters

    # selecting letters, symbols and numbers
    letters = [random.choice(characters["letters"]) for _ in range(0, num_letters)]
    symbols = [random.choice(characters["symbols"]) for _ in range(0, num_symbols)]
    numbers = [random.choice(characters["numbers"]) for _ in range(0, num_numbers)]

    # creating password
    password = letters + symbols + numbers
    random.shuffle(password)
    password = ''.join(password)

    # giving password to user
    pyperclip.copy(password)
    password_entry.insert(0, password)


def save_password():
    """This function checks if the user filled every entry. If not, it just shows a error message
     If he has, it creates a pop up to ask the user if he wants to save the password
     It saves the username and password to the passwords.txt file
    It also deletes the text writen in the entries"""
    # getting information from entries
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "username": username,
            "password": password
        }
    }
    # checking for empty entries
    if not website or not username or not password:
        messagebox.showinfo(title="Error", message="Oops, please don't leave any field empty")
    else:
        # creating pop up
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail/Username: "
                                                              f"{username}\nPassword: {password}\nIs it ok to save?")
        # saving to file
        if is_ok:
            try: # checking for error it the file hasn't been created yet
                # opening old data
                with open("passwords.json", "r") as f:
                    data = json.load(f)
            except (FileNotFoundError, JSONDecodeError):
                # creating file with write mode
                with open("passwords.json", "w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                # updating new_data
                data.update(new_data)
                with open("passwords.json", "w") as f:
                    # putting new data in file
                    json.dump(data, f, indent=4)
            finally:
                # deleting entries
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def search_password():
    # saving current website
    website = website_entry.get()
    # open current passwords
    try:
        with open("passwords.json", "r") as f:
            data = json.load(f)
        username = data[website]["username"]
        password = data[website]["password"]
        messagebox.showinfo(title=f"{website}", message=f"Username/Email: {username}\nPassword: {password}")

    except (FileNotFoundError, JSONDecodeError):
        messagebox.showinfo(title="Empty database", message="Looks like you haven't added any passwords yet")
        # deleting entries
        website_entry.delete(0, END)
        password_entry.delete(0, END)
    except KeyError:
        messagebox.showinfo(title="No website", message="The website you are looking for doesn't exist in the database")
        # deleting entries
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# UI setup
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=2, row=1)

# labels
# website label
website_label = Label(text="Website:   ", font=("Arial", 12))
website_label.grid(column=1, row=2, sticky="E", pady=1)
# email/username
username_label = Label(text="Email/Username:   ", font=("Arial", 12))
username_label.grid(column=1, row=3, sticky="E", pady=1)
# password label
password_label = Label(text="Password:   ", font=("Arial", 12))
password_label.grid(column=1, row=4, sticky="E", pady=1)

# entries
# website entry
website_entry = Entry(width=33)
website_entry.grid(column=2, row=2, columnspan=2, sticky="W")
website_entry.focus()
# email/username entry
username_entry = Entry(width=52)
username_entry.grid(column=2, row=3, columnspan=2, sticky="W")
username_entry.insert(0, "arturcaminero@gmail.com")
# password entry
password_entry = Entry(width=33)
password_entry.grid(column=2, row=4, sticky="W")

# buttons
# generate password button
generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(column=3, row=4, sticky="W")
# add button
add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(column=2, row=5, columnspan=2, pady=1)
# search button
search_button = Button(text="Search", width=14, command=search_password)
search_button.grid(column=3, row=2, pady=1, sticky="W")

# mainloop
mainloop()

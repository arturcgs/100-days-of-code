# Password Generator
import random

# input
from Tools.scripts.nm2def import symbols

length = int(input("How many characters do you want in your password? "))

# characters dict
characters = {"letters": ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                          's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
              "symbols": ["!", "@", "#", "$", "%", "&", "*", "(", ")", "|", "[", "]", "{", "}", ":", ",", ".", "<",
                          ">", ";", "?", "/", "+"],
              "numbers": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]}

# how many letters, symbols ans numbers the password will have, chosen randomly
num_letters = random.randint(1, length)
num_symbols = random.randint(1, (length - num_letters))
num_numbers = length - num_symbols - num_letters

# creating password
password = []

# selecting letters
for _ in range(0, num_letters):
    password.append(random.choice(characters["letters"]))

# selecting symbols
for _ in range(0, num_symbols):
    password.append(random.choice(characters["symbols"]))

# selecting numbers
for _ in range(0, num_numbers):
    password.append(random.choice(characters["numbers"]))



# shuffling the password letters
random.shuffle(password)

print(f" Your password is: {''.join(password)}")
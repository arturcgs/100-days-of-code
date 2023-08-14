from morse_code import morse_code

to_translate = input("Hello!\nWelcome to the Morse Code Translator!!\nWhat phrase would you like to translate:\n")\
    .lower()

translated = ""
for char in to_translate:
    translated += morse_code[char] + " "

print(f"Here is your translated phrase:\n{translated}")

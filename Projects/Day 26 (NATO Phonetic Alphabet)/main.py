# creating alphabet list
alphabet = [chr(i) for i in range(97, 123)]

# creating NATO phonetic alphabet list
NATO = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima",
        "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey",
        "X-ray", "Yankee", "Zulu"]

# creating alphabet do NATO dictionary
alphabet_to_NATO = {letter: nato_word for letter, nato_word in zip(alphabet, NATO)}
print(alphabet_to_NATO)

# asking user for input
to_translate = input("What word would you like to translate to NATE Phonetic Alphabet?\n").lower().strip()
translated_word = [alphabet_to_NATO[letter] for letter in to_translate]
print("-".join(translated_word))

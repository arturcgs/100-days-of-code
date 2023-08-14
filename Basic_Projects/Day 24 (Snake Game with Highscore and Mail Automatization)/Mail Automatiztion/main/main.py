
# reading letter
with open("../Input/Letters/starting_letter.txt") as f:
    letter = f.read()

# reading names
with open("../Input/Names/invited_names.txt") as names_file:
    for name in names_file:
        name = name.strip()
        with open(f"../Output/ReadyToSend/letter_for_{name}.txt", "w") as output_letter:
            output_letter.write(letter.replace("[name]", name))

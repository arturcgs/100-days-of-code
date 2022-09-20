print("Welcome! This program encodes a message with the Caesar Cipher method.\n")

def caesar(cipher_direction):
    #inputs
    message = input('What is the message you want to encode? ').lower().strip()
    shift = int(input("What is the shift you want to apply? ")) % 26

    # initiating encoded message
    new_message = ''

    for letter in message:
        if 97 <= ord(letter) <= 122: #check if it is letter
            # encoding
            if cipher_direction == 'encode':
                letter_shift = ord(letter) + shift
                if letter_shift > 122: #cheks if need to loop around the alphabet
                    new_letter = chr(letter_shift - 26)
                else:
                    new_letter = chr(letter_shift)
            #deciphering
            else:
                letter_shift = ord(letter) - shift
                if letter_shift < 97: #check if need to loop around alphabet
                    new_letter = chr(letter_shift + 26)
                else:
                    new_letter = chr(letter_shift)

            new_message += new_letter # add new letter
        else: # keeps non letters
            new_message += letter
    print(f"This is your new message: {new_message}")

while True:
    program_choice = input("What do you want to do?\nType 'encode', 'decipher' or anything else to exit.\n").strip().lower()
    if program_choice == 'encode' or program_choice == 'decipher':
        caesar(program_choice)
    else:
        print("Thank you for using my program!")
        break


# first challenge
# leap year

def leap_year():
    year = int(input('What is the year you want to check: '))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("This is a leap year!")
            else:
                print("This is not a leap year")
        else:
            print("This is a leap year!")
    else:
        print("This is not a leap year")

leap_year()

# second challange
# love calculator

def love_calculator():
    #inputs
    name1 = input("What is your name? ").strip().lower()
    name2 = input("What is your crush's name? ").strip().lower()

    # joining names and creating counter
    names = name1 + name2
    love_counter = {'t': 0, "r": 0, "u": 0, "e": 0, "l": 0, "o": 0, "v": 0}

    #counting
    for letter in names:
        if letter in 'truelov':
            love_counter[letter] += 1

    # adding the word's numbers
    true = love_counter['t'] + love_counter['r'] + love_counter['u'] + love_counter['e']
    love = love_counter['l'] + love_counter['o'] + love_counter['v'] + love_counter['e']
    score = int(str(true) + str(love))

    # printing the result
    print(f"\nT - {love_counter['t']}   |   L - {love_counter['l']}\n"
          f"R - {love_counter['r']}   |   O - {love_counter['o']}\n"
          f"U - {love_counter['u']}   |   V - {love_counter['v']}\n"
          f"E - {love_counter['e']}   |   E - {love_counter['e']}\n"
          f"-----------------\n"
          f"       {score}%")

    # sending message
    if score < 10 or score > 90:
        print(f"\nYour score is {score}, you go together like coke and mentos.")
    elif 40 <= score <= 50:
        print(f"\nYour score is {score}, you are alright together")
    else:
        print(f"\nYour score is {score}")

love_calculator()


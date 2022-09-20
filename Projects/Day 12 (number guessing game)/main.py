import random
from art import logo

def game():
    # welcome message
    print(logo)

    # difficulty selection
    print('\nDifficulty levels:'
          '\n(1) Easy\n(2) Medium\n(3) Hard\n(0) Exit')
    difficulty = int(input('Select difficulty: '))

    if difficulty == 1:
        total_tries = 20
    elif difficulty == 2:
        total_tries = 10
    elif difficulty == 3:
        total_tries = 5
    elif difficulty == 0:
        total_tries = 0
    else:
        print('Invalid command')

    # points
    points = 1000

    # secret value
    secret_number = random.randint(1, 101)

    for i in range(0, total_tries):
        # getting guess
        guess = int(input('\nType a number between 1 and 100: '))

        # not allowed guesses
        if guess > 100 or guess < 1:
            print('Invalid number. Try again.')
            print(f'You have {total_tries - (i + 1)} tries left')
            points = points - abs(guess - secret_number)
            continue

        # definindo bigger, bigger10, same, smaller10 e smaller
        bigger = guess > secret_number + 10
        bigger10 = secret_number + 10 >= guess > secret_number
        same = guess == secret_number
        smaller10 = secret_number - 10 <= guess < secret_number
        smaller = guess < secret_number - 10

        #informando localização do guess
        if bigger:
            print('Way too high')
        elif bigger10:
            print("You're a bit higher")
        elif same:
            print("You got it!")
            print(f'Your score is {points} points')
            break
        elif smaller10:
            print("You're a bit lower")
        elif smaller:
            print('Way too low')

        #número de tentativas restantes
        print(f'You have {total_tries - (i + 1)} tries left')

        #subtraindo points
        points = points - abs(guess - secret_number)

    print('End of game!')

game()

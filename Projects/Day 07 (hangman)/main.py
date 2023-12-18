import random
import hangman_sprites
import hangman_words

def hangman():
    # welcome message
    print(hangman_sprites.logo)

    # importing the words
    words = hangman_words.word_list

    # selecting a random word
    secret_word = words[random.randint(0, len(words))]

    player_attempt_list = []
    index_list = []
    errors = 0

    # decide random arm and leg
    random_arm = random.randint(20, 21)
    random_leg = random.randint(40, 41)

    # initial message
    print('Secret word:\n' + "_ " * len(secret_word))

    while True:
        # printing the hangman
        if errors == 2:
            print(hangman_sprites.stages[random_arm])
        elif errors == 4:
            print(hangman_sprites.stages[random_leg])
        else:
            print(hangman_sprites.stages[errors])

        player_attempt = input('Choose a letter: ').strip().lower()

        if player_attempt in player_attempt_list:
            print("You've already tried that letter.")
            continue
        else:
            player_attempt_list.append(player_attempt)

        # correct letter
        index = 0
        if player_attempt in secret_word:
            print()
            for letter in secret_word:
                if player_attempt == letter:
                    index_list.append(index)
                index += 1
        # wrong letter
        else:
            errors += 1
            print(f'This letter is not in the word\nYou used {errors} out of 6 possible errors\n')

        # defeat check
        if errors == 5:
            print(hangman_sprites.stages[5])
            print(f'You lost!\nThe word was {secret_word}')
            break

        # victory check
        if len(index_list) == len(secret_word):
            print(secret_word)
            print('Congratulations! You found the secret word!')
            break

        # printing the word
        print("Secret word:")
        for i in range(0, len(secret_word.capitalize())):
            if i in index_list:
                print(f"{secret_word[i]} ", end='')
            else:
                print("_ ", end='')
        print(f"\nYou have tried these letter: {' - '.join(sorted(player_attempt_list))}")

hangman()
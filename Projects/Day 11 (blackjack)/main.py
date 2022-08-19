from art import logo
import random


def deal_card():
    """returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def print_hands(player_hand, player_score, computer_hand):
    """This function prints the player hand, score and the computer hand"""
    print(f"\tYour cards: {player_hand}, current score: {player_score}")
    print(f"\tComputer's first card: {computer_hand[0]}")


def get_new_card(hand_of_cards, score):
    """This function adds a new card to a hand of cards"""
    # save new card
    new_card = deal_card()

    # check if Ace
    if new_card == 11:
        if score + 11 > 21:
            new_card = 1

    # update player_hand and player_score
    hand_of_cards.append(new_card)
    score = sum(hand_of_cards)

    return hand_of_cards, score


def compare(player_score, computer_score):
    """This function compares who won the game, and why.
    It returns a string with the final message"""
    if player_score > 21:
        return "You went over, you lose 😤"
    elif computer_score > 21:
        return "The computer went over, you win 😁"
    elif player_score == computer_score:
        return "It's a draw 🙃"
    elif player_score == 21:
        return "You win with a blackjack 😎"
    elif computer_score == 21:
        return "Computer has a blackjack, you lose 😱"
    elif player_score > computer_score:
        return "You are closer to 21, you win 😃"
    else:
        return "The computer is closer to 21, you lose 😤"



def clear():
    # I am using pycharm, so clear() from replit doesn't work
    print("\n" * 100)


def blackjack():
    # printing logo
    print(logo)

    # initial hands
    player_hand = [deal_card()]
    computer_hand = [deal_card()]

    # adding the second card
    # I need to use the function to avoid getting a 22 as initial cards
    player_hand, player_score = get_new_card(player_hand, player_hand[0])
    computer_hand, computer_score = get_new_card(computer_hand, computer_hand[0])

    # printing initial hands
    print_hands(player_hand, player_score, computer_hand)

    # player buying cards
    while player_score <= 21 and input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
        # get a new card
        player_hand, player_score = get_new_card(player_hand, player_score)

        # print new hand
        print_hands(player_hand, player_score, computer_hand)

    # computer buying cards
    while computer_score < 17:
        computer_hand, computer_score = get_new_card(computer_hand, computer_score)

    # printing final score
    print("-" * 60)
    print(f"\tYour final hand: {player_hand}, final score: {player_score}")
    print(f"\tComputer's final hand: {computer_hand}, final score {computer_score}")

    # comparing to see who won
    print(compare(player_score, computer_score))


while input("Would you like to play a game of blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    blackjack()
print("Thanks for playing!")

from game_data import data
from art import logo, vs
import random


def player_is_right(influencer1, influencer2, player_choice):
    """Returns True if the user got it right, and False if he got ir wrong"""
    if influencer1['follower_count'] >= influencer2['follower_count']:
        return player_choice == 'a'
    else:
        return player_choice == 'b'


def clear():
    """I am using pycharm, so this is how I can clean the console"""
    print("\n" * 100)


def higher_lower():
    # print logo
    print(logo)

    # pick a random influencer
    influencer2 = random.choice(data)
    # removing influencer, so that it doesn't repeat
    data.remove(influencer2)

    # initiating score and player_lost
    score = 0
    player_lost = False

    while not player_lost:
        # set influencer 1 to be influencer2
        influencer1 = influencer2
        # print his description and country
        print(f"Compare A: {influencer1['name']}, a {influencer1['description']} from {influencer1['country']}")

        #print versus
        print(vs)

        # pick a second influencer
        influencer2 = random.choice(data)
        # removing influencer, so that it doesn't repeat
        data.remove(influencer2)
        # print his description and country
        print(f"Against B: {influencer2['name']}, a {influencer2['description']} from {influencer2['country']}")

        # ask the user which one has more subscribers
        player_choice = input("Who do you think has more subscribers? Type 'A' or 'B': ").lower().strip()


        #clear and logo
        clear()
        print(logo)
        # check is he got it right
        if player_is_right(influencer1, influencer2, player_choice):
            score += 1
            print(f"You're right! Your current score is {score}")
        # lose if wrong
        else:
            player_lost = True
            print(f"Sorry, you're wrong. You got a score of {score}")

higher_lower()
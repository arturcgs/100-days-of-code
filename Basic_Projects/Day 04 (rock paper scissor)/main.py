import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = ['', rock, paper, scissors]

move_names = ['', 'rock', 'paper', 'scissors']

win_check = {'13': 'You won!', '12': 'You lost', '11': "It's a tie!",
             '21': 'You won!', '23': 'You lost', '22': "It's a tie!",
             '32': 'You won!', '31': 'You lost', '33': "It's a tie!"}

print("Welcome to rock, paper scissors!")

while True:
    player_move = int(input("Type 1 for rock, 2 for paper and 3 for scissors\n"
                            "You can also type 0 to exit\n"))
    #exit
    if not player_move:
        print("Thanks or playing!")
        break
    if player_move < 0 or player_move > 3:
        print("You typed a invalid number!")
        break

    #printing player option
    print(f"You played {move_names[player_move]}")
    print(game_images[player_move])

    #getting and printing computer move
    computer_move = random.randint(1, 3)
    print(f'The computer played {move_names[computer_move]}')
    print(game_images[computer_move])

    #checking who won
    game = str(player_move) + str(computer_move)
    print(win_check[game])
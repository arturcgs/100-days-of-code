
def bidding():
    #inputs
    name = input("What if your name? ").capitalize().strip()
    value = int(input("What's your bid? "))
    #add to dict
    bids[name] = value

def clear():
    # as I am using pycharm, I can't really clear the console
    print("\n" * 100)


# printing logo
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
print("Welcome to the Silent Auction!")

#initiating variables
bids = {}
more_bidders = True

# getting every bid
while more_bidders:
    print()
    bidding()

    more_bidders_check = input("Is there another bidder? ")
    clear()

    if more_bidders_check == 'no':
        more_bidders = False

highest_bidder = max(bids, key=bids.get)
print(f"\nCongratulations {highest_bidder}, you won with a bid of ${bids[highest_bidder]:.2f}")
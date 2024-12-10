import os

logo = r'''
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
'''

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
print(logo)
print("Welcome to the secret auction program.")

taking_bids = True
bids = {}

while taking_bids:
  while True:
    name = input("What is your name?: ")
    try:
      existing_name = bids[name]
      print("Somebody else with that name has already bid. Please use a different name.")
    except KeyError:
      break
  bid = int(input("What's your bid?: £"))
  bids[name] = bid
  while True:
    new_bid = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if (new_bid.lower() == 'yes' or new_bid.lower() == 'no'):
      clear_screen()
      break
    else:
      print("I didn't understand what you wrote; please try again.")
  if new_bid == 'no':
    taking_bids = False

max_bid = 0
bidder = ''
for person in bids:
  if bids[person] > max_bid:
    max_bid = bids[person]
    bidder = person

print(f"The winner is {bidder} with a bid of £{max_bid}")
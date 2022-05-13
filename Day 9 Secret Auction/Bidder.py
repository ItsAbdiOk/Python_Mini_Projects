import os
import art
clear = lambda: os.system('cls')
print(art.logo)
print("Welcome to the secret auction program.")
Finished_Bidding = False
New_Bid = {}

while not Finished_Bidding:   
    name = input("What is your name? :")
    bid_price = input("What is your bid? : $")
    New_Bid[name] = int(bid_price)
    Finished = input("Are there any more bidders? yes or no.")
    if Finished == "no":
        Finished_Bidding = True
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(art.logo)

   
Highest_Bid = 0
Current_winner = ""

for bidder in New_Bid:
    current_bid = int(New_Bid[bidder])
    if current_bid > Highest_Bid:
        Highest_Bid = current_bid
        Current_winner = bidder

print(f"This highest Bid is ${Highest_Bid} with from {Current_winner} ")
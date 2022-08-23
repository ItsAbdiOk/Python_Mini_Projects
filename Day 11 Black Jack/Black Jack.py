from logo import logo
import sys

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
User_Total = 0
def drawing_cards(Hand1, Hand2):
    Hand1 = list(random.choices(cards, k = 2))
    Hand2 = list(random.choices(cards, k = 2))
    while sum(Hand2) <= 16:
        Hand2.append(random.choice(cards)) 
    return Hand1,Hand2

def Winner_Checker(User,Deal):
    User_Total = sum(User)
    Dealer_Total = sum(Deal)
    if 11 in User and User_Total > 22:
        User.remove(11)
        User.append(1)
    if User_Total > Dealer_Total and User_Total < 22:
       print("You win")
    elif User_Total > 21:
        print("You lose, Sassy Baka")

def Hand_checker(User):
    User_Total = sum(User)
    if User_Total > 21:
        print("You lose, Sassy Baka")

def Main():
    First_Card = 0
    Dealer = []
    User_Hand = [] 
    print(logo)
    User_Hand,Dealer = drawing_cards(User_Hand,Dealer)
    print(f"Your hand is {User_Hand[1]} and {User_Hand[1]}, which is a total of {User_Hand[1] + User_Hand[1]}")
    if User_Hand[0] + User_Hand[1] == 21:
        Winner = True 
        return Winner
    First_Card = Dealer[0]
    print(f"The Dealer's hand is {First_Card}")
    Next_Turn = input("Type 'y' to get another card, type 'n' to fold: ")
    if Next_Turn == "n":
        print("cringe")
        Winner_Checker(User_Hand,Dealer)
    elif Next_Turn == "y":
        User_Hand.append(random.choice(cards)) 
        Hand_checker(User_Hand)
            
Main()
    

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

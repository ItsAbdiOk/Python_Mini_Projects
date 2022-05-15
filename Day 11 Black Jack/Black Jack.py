from logo import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
User_Total = 0
def drawing_cards(Hand1, Hand2):
    Hand1 = list(random.choices(cards, k = 2))
    Hand2 = list(random.choices(cards, k = 2))
    while sum(Hand2) <= 16:
        Hand2.append(random.choice(cards)) 
    return Hand1,Hand2

def Winner_Checker(User,Deal,win,lose):
    User_Total = sum(User)
    Dealer_Total = sum(Deal)
    if User_Total > Dealer_Total and User_Total > 22:
        win = True
        return win
    else:
        lose = True
        return lose


def Main():
    Winner = False
    Loser = False
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
        return Winner_Checker(User_Hand,Dealer,Winner,Loser)

if __name__ == '__main__':
    Game_Status = Main()
    
